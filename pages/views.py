from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from markethub.models import *
from .models import Corper_blog, Comment, Vacancy
from .tasks import *
from django.contrib.auth.decorators import login_required
from markethub.models import *
from skillhub.models import *


def index(request):
    blog = Corper_blog.objects.order_by('-publish')[:5]
    vacant = Vacancy.objects.order_by('-publish')[:5]
    vacant_two = Vacancy.objects.order_by('-publish')[5:10]
    product = Product.objects.order_by('-date')[:1]
    product_two = Product.objects.order_by('-date')[1:2]
    skill = Artisan.objects.order_by('-date')[:1]
    skill_two = Artisan.objects.order_by('-date')[1:2]
    context = {
        'blog':blog, 
        'vacant':vacant, 
        'vacant_two':vacant_two, 
        'product':product, 
        'product_two':product_two, 
        'skill':skill,
        'skill_two':skill_two,
        }
    # import task to delete blogs
    delete_blog_posts()
    return render(request, 'pages/index.html', context)

def post_detail(request, detail_id , post):
    post_details = get_object_or_404(Corper_blog, pk=detail_id, slug=post)
    # get all comments for the psot
    comments = post_details.comments.filter(active=True)

    if request.method == 'POST':
        body = request.POST['comment']
        post = post_details

        com = Comment(body=body, post=post, )
        com.author = request.user
        com.save()
        return redirect(post_details.get_absolute_url())
        
        
    context = {'post_details': post_details, 'comments': comments}
    return render(request, 'pages/post_detail.html', context)

@login_required(login_url='/accounts/login')
def vacancies(request):
    vacan = Vacancy.objects.filter(state__contains=request.user.state)
    context = {'vacan': vacan}
    return render(request, 'pages/vacancies.html', context)

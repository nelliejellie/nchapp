from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from markethub.models import *
from .models import Corper_blog, Comment
from .tasks import *


def index(request):
    blog = Corper_blog.objects.order_by('-publish')[:5]
    context = {'blog':blog}
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
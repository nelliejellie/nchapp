from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from markethub.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def markethub(request):
    products = Product.objects.filter(user__state__contains=request.user.state) #filter the products by the state of the user
    if len(products) < 1:
        messages.success(request, 'no products uploaded in your state yet')
    if request.method == 'POST':
        query = request.POST['options']
        print(query)
        products = Product.objects.filter(categories__iexact=query)
        context = {'products':products}
        return render(request, 'markethub/search_product.html', context)
    context = {
        'products':products,
    }
    return render(request, 'markethub/markethub.html', context)

def product_form(request):
    if request.method == 'POST':
        name = request.POST['product_name']
        descriptions = request.POST['description']
        price = request.POST['price']
        categories = request.POST['category']
        image = request.FILES.get('image')
        image_two =  request.FILES.get('image_two')
        image_three = request.FILES.get('image_three')
        number = request.POST['number']

        product = Product(name=name, descriptions=descriptions, price=price, categories=categories, image=image, image_two=image_two, image_three=image_three, contact_number=number)
        product.user = request.user
        product.save()
        subject = 'product uploaded to naijacorphub'
        message = f'Hi {product.user.username} thanks for registering with us. your product has been uploaded'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [product.user.email,]
        send_mail(subject, message, from_email, recipient_list)
        return redirect('markethub')
    return render(request, 'markethub/market_form.html')

def product_detail(request, product_id):
    details = get_object_or_404(Product, pk=product_id)
    context = {'details': details}
    return render(request, 'markethub/product_detail.html', context)

def search_product(request):
    return render(request, 'markethub/search_product.html')
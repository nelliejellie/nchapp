from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from markethub.models import *


def markethub(request):
    products = Product.objects.order_by('-date')
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

        product = Product(name=name, descriptions=descriptions, price=price, categories=categories, image=image, image_two=image_two, image_three=image_three)

        product.save()
        return redirect('markethub')
    return render(request, 'markethub/market_form.html')

def product_detail(request, product_id):
    details = get_object_or_404(Product, pk=product_id)
    context = {'details': details}
    return render(request, 'markethub/product_detail.html', context)
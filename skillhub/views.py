from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def skillhub(request):    
    return render(request, 'skillhub/skillhub.html')


def carpenter(request):
    artisan = Artisan.objects.filter(categories='Carpenter')
    context = {'artisan': artisan}
    return render(request, 'skillhub/carpenter.html', context)

def electrician(request):
    artisan = Artisan.objects.filter(categories='Electrcian')
    return render(request, 'skillhub/electrician.html')

def realtor(request):
    artisan = Artisan.objects.filter(categories='Realtor')
    return render(request, 'skillhub/realtor.html')

def pers_shop(request):
    artisan = Artisan.objects.filter(categories='Personal-Shopper')
    return render(request, 'skillhub/pers_shop.html')

def beautician(request):
    artisan = Artisan.objects.filter(categories='beautician')
    return render(request, 'skillhub/beautician.html')

def hair_dresser(request):
    artisan = Artisan.objects.filter(categories='Hair-dresser')
    return render(request, 'skillhub/hair_dresser.html')

def barber(request):
    artisan = Artisan.objects.filter(categories='Barber')
    return render(request, 'skillhub/barber.html')

def fashion_designer(request):
    artisan = Artisan.objects.filter(categories='Fashion-designer')
    return render(request, 'skillhub/fashion_designer.html')

def painter(request):
    artisan = Artisan.objects.filter(categories='Painter')
    return render(request, 'skillhub/painter.html')

def photographer(request):
    artisan = Artisan.objects.filter(categories='Photographer')
    return render(request, 'skillhub/photographer.html')

def baker(request):
    artisan = Artisan.objects.filter(categories='Baker')
    return render(request, 'skillhub/baker.html')

def soft_dev(request):
    artisan = Artisan.objects.filter(categories='Software-developer')
    return render(request, 'skillhub/soft_dev.html')

def skill_detail(request, skill_id):
    artisan = get_object_or_404(Artisan, pk=skill_id)
            
    context = {'artisan': artisan}
    return render(request, 'skillhub/skill_detail.html', context)

def artisan_form(request):
    if request.method == 'POST':
        descriptions = request.POST['description']
        contact_number = request.POST['contact']
        categories = request.POST['category']
        image = request.FILES.get('image')
        image_two =  request.FILES.get('image_two')
        image_three = request.FILES.get('image_three')

        artisan = Artisan(descriptions=descriptions,categories=categories,contact_number=contact_number, image=image, image_two=image_two, image_three=image_three)

        artisan.save()
        return redirect('skillhub')
    return render(request, 'skillhub/skill_form.html')
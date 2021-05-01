from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .models import MyUser
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.conf import settings


# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password_two = request.POST['password2']
        email = request.POST['email']
        reg_no = request.POST['reg_no']
        state = request.POST['state']
        local_govt = request.POST['local_govt']

        #check if password match
        if password == password_two:
            # check if username exists
            if MyUser.objects.filter(username=username).exists():
               messages.error(request,'username exists') 
               return redirect('register')
            else:
                if MyUser.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    # looks good
                    user = MyUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, 
                                                    password=password, reg_no=reg_no, state=state, local_govt=local_govt, email=email)
                    user.is_active = False
                    user.save()
                    messages.success(request, ' welcome Corper!!!Your account will be active once your registeration number is confirmed')
                    subject = 'welcome to naijacorphub'
                    message = f'Hi {user.username} thanks for registering with us. Once your reg no({user.reg_no}) is confirmed your account will be activated'
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [user.email,]
                    send_mail(subject, message, from_email, recipient_list)
                    return redirect('index')
        else:
            messages.error(request,'password must match')
            return redirect('register')
        messages.error(request,'something went wrong!! try again')
    else:   
        return render(request, "accounts/register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                dj_login(request,user)
                messages.success(request,'logged in')
                return redirect('index')
            else:
                messages.error(request,'disabled account')
                return redirect('login')
        else:
            messages.success(request,'invalid account')
            return redirect('login')

    return render(request, "accounts/login.html")

def logout(request):
    if request.method == 'POST':
        dj_logout(request)
        messages.success(request,'you have successfully logged out')
        return redirect('index')


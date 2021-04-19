from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from markethub.models import *


def index(request):
    return render(request, 'pages/index.html')
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello world. You are at home page')
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse('Hello world. You are at About page')

def contact(request):
    return HttpResponse('Hello world. You are at contact page')


from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def sistema(request):
    return render(request, 'sistema.html')


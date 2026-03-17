from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Página Inicial</h1>')

def index(request):
    return render(request,'djangoApp/index.html')

def dashboard(request):
    return render(request,'djangoApp/dashboard.html')
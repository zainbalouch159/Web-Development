from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home(req):
    return render(req,'home.html')

def navbar(req):
    return render(req,'./components/navbar.html')

def search(req):
    name= req.GET.get('q')
    return HttpResponse(f"Search {name}")
def product(req):
     return HttpResponse("product ")

def contact(req):
     return HttpResponse("contact ")
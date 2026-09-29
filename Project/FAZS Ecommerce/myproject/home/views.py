from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import Product,Category,Collection,Hero

# Create your views here.

def home(req):
    product = Product.objects.all()
    category = Category.objects.all()
    collection = Collection.objects.all()
    hero = Hero.objects.first()
    return render(req,'home.html',{'products':product, 'Categories': category, 'Collections':collection, 'hero':hero})


def search(req):
    name= req.GET.get('q')
    return HttpResponse(f"Search {name}")

def product(req):
     return HttpResponse("product ")

def contact(req):
     return render(req,'contact.html')
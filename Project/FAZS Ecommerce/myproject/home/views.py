from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import Product,Category,Collection,Hero
from django.db.models import Count

# Create your views here.

# Home 
def home(req):

    product = Product.objects.all()

    category = Category.objects.annotate(
        product_count=Count('product')
    ).filter(product_count__gt=0)

    collection = Collection.objects.annotate(
        product_count=Count('product')
    ).filter(product_count__gt=0)

    hero = Hero.objects.first()

    return render(req, 'home.html', {
        'products': product,
        'Categories': category,
        'Collections': collection,
        'hero': hero
    })
    
# Search Animation     
def search(req):
    name= req.GET.get('q')
    return HttpResponse(f"Search {name}")

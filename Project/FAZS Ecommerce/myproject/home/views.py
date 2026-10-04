from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import Product,Category,Collection,Hero
from django.db.models import Count, Case, When, IntegerField 

# Create your views here.

# Home 
def home(req):

    product = Product.objects.all()

    category = Category.objects.annotate(
        other_last=Case(
            When(name__iexact="other", then=1),
            default=0,
            output_field=IntegerField(),
        )
    ).order_by("other_last", "name")

    collection = Collection.objects.exclude(
        title__iexact="other"
    ).order_by("title")

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

# Category Products
def category_products(req, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)

    return render(req, 'components/category_products.html', {
        'category': category,
        'products': products
    })

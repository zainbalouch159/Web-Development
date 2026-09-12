from django.shortcuts import render,redirect
from product.models import Category,Product,Collection
from django.http import JsonResponse

# Create your views here.

def dashboard(req):
    category = Category.objects.all()
    product =Product.objects.all()
    collection =Collection.objects.all()
    return render(req,'dashboard.html',{'Products':product,'Categories':category,'Collections':collection})

def add_product(req):
    Name = req.POST.get('Name')
    Description = req.POST.get('Description')
    Price = req.POST.get('Price')
    Stock = req.POST.get('Stock')
    image = req.POST.get('image')
    Discount = req.POST.get('Discount')
    Info = req.POST.get('Info')
    Category = req.POST.get('Category')
    Collections = req.POST.get('Collections')
    
def add_category(req):
    new_category =  req.POST.get('category-name')
    if new_category:
        category=Category(
            name=new_category
        )
        category.save()
        
        return JsonResponse({
            'id':category.id,
            'name':category.name
        })
        
def add_Collections(req):
    new_collection =  req.POST.get('collection-name')
    if new_collection:
        collection=Collection(
            name=new_collection
        )
        collection.save()
        
        return JsonResponse({
            'id':collection.id,
            'name':collection.name
        })
       
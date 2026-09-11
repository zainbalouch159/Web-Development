from django.shortcuts import render,redirect
from product.models import Category,Product

# Create your views here.

def dashboard(req):
    category = Category.objects.all()
    product =Product.objects.all()
    return render(req,'dashboard.html',{'Products':product,'Categories':category},)

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
       
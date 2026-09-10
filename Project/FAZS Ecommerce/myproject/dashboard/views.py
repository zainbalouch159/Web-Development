from django.shortcuts import render

# Create your views here.

def dashboard(req):
    return render(req,'dashboard.html')

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
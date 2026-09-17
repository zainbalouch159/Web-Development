from django.shortcuts import render,redirect, get_object_or_404
from product.models import Category,Product,Collection
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

@login_required
def dashboard(req):
    category = Category.objects.all()
    product =Product.objects.all()
    collection =Collection.objects.all()
    return render(req,'dashboard.html',{'Products':product,'Categories':category,'Collections':collection})
    
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
            title=new_collection
        )
        collection.save()
        
        return JsonResponse({
            'id':collection.id,
            'title':collection.title
        })
       
def add_product(req):
    Name = req.POST.get('name')
    Description = req.POST.get('description')
    Price = req.POST.get('price')
    Stock = req.POST.get('stock')
    image = req.FILES.get('image')
    Discount = req.POST.get('discount')
    if not Discount:
        Discount=0
    Info = req.POST.get('info') 
    Category_id = req.POST.get('category')
    Collections_id = req.POST.get('collections')
    if Category_id == 'Select' or not Category_id:
        Category1, created=Category.objects.get_or_create(name='other')
    else:
        Category1 = Category.objects.get(id=Category_id)
        
    if Collections_id == 'Select' or not Collections_id:
        Collections, created=Collection.objects.get_or_create(title = 'other')
    else:
        Collections = Collection.objects.get(id=Collections_id)

    product =Product(
        name = Name,
        description = Description,
        price = Price,
        stock = Stock,
        image = image,
        discount = Discount,
        info = Info,
        category = Category1,
    )
    product.save()
    product.collections.add(Collections)
    return JsonResponse({
        'id': product.id,
        'name' : product.name,
        'price' : product.price,
        'stock': product.stock,
        'sales' : product.sales,
        'image' : product.image.url,
       
    })
    
def product_delete(req,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('dashboard')

def product_edit(req,id):
    pass
    
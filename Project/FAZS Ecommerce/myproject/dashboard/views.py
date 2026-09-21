from django.shortcuts import render,redirect, get_object_or_404
from product.models import Category,Product,Collection
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here

# Dashboard
@login_required
def dashboard(req):
    if req.user.is_staff:
        category = Category.objects.all()
        product =Product.objects.all()
        collection =Collection.objects.all()
        return render(req,'dashboard.html',{'Products':product,'Categories':category,'Collections':collection})
    else:
        return redirect('home')

# Add Category
@require_POST    
def add_category(req):
    new_category =  req.POST.get('category-name')
    if new_category:
        category, created=Category.objects.get_or_create(name=new_category)

        
        return JsonResponse({
            'id':category.id,
            'name':category.name
        })
        
# Add Collections
@require_POST         
def add_Collections(req):
    new_collection =  req.POST.get('collection-name')
    if new_collection:
        collection, created=Collection.objects.get_or_create(
            title=new_collection
        )
        return JsonResponse({
            'id':collection.id,
            'title':collection.title
        })

# Add Product
def add_product(req):
    Name = req.POST.get('name')
    Description = req.POST.get('description')
    Price = req.POST.get('price')
    Stock = req.POST.get('stock')
    image = req.FILES.get('image')
    Discount = req.POST.get('discount')
    
    if not Discount:
        Discount = 0

    Info = req.POST.get('info')

    Category_id = req.POST.get('category')
    Collections_id = req.POST.getlist('collections')

    # Category
    if Category_id == 'Select' or not Category_id:
        Category1, created = Category.objects.get_or_create(name='other')
    else:
        Category1 = Category.objects.get(id=Category_id)

    # Collections
    if not Collections_id or 'Select' in Collections_id:
        Collections = Collection.objects.filter(title='other')
        if not Collections.exists():
            other_collection = Collection.objects.create(title='other')
            Collections = [other_collection]
    else:
        Collections = Collection.objects.filter(id__in=Collections_id)

    # Product
    product = Product(
        name=Name,
        description=Description,
        price=Price,
        stock=Stock,
        image=image,
        discount=Discount,
        info=Info,
        category=Category1,
    )

    product.save()

    # Multiple collections
    product.collections.set(Collections)

    return redirect('dashboard')
    
# Product Delete
@require_POST
def product_delete(req,id):
    product = get_object_or_404(Product, id=id)
    if product.image:
        product.image.delete()
    if product:  
        product.delete()
        return JsonResponse('success', safe=False)
    else:
        return JsonResponse('failed', safe=False)

def product_edit(req,id):
    product = Product.objects.get(id=id)    
    data ={
        'name':product.name,
        'description':product.description,
        'price':product.price,
        'sales':product.sales,
        'stock':product.stock,
        'discount':product.discount,
        'info':product.info,
        'image':product.image.url,
        'category':product.category.id,
        'collections':list(product.collections.values_list('id', flat=True)),
    }
    return JsonResponse(data)
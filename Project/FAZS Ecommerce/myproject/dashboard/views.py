from django.shortcuts import render,redirect, get_object_or_404
from product.models import Category,Product,Collection
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

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

# Add Category in product form 
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
    product.image.delete()
    if product:  
        product.delete()
        return JsonResponse('success', safe=False)
    else:
        return JsonResponse('failed', safe=False)

# Edit Product
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

# Update Product 
def update_product(req):
    id= req.POST.get('product_id')
    product = Product.objects.get(id=id)

    product.name = req.POST.get('name')
    product.description = req.POST.get('description')
    product.price = req.POST.get('price')
    product.stock = req.POST.get('stock')

    discount = req.POST.get('discount')
    product.discount = discount if discount else 0

    product.info = req.POST.get('info')

    # Category
    category_id = req.POST.get('category')

    if not category_id or category_id == 'Select':
        category, created = Category.objects.get_or_create(name='other')
    else:
        category = Category.objects.get(id=category_id)

    product.category = category

    # Image
    image = req.FILES.get('image')

    if image:
        product.image = image

    product.save()

    # Collections
    collection_ids = req.POST.getlist('collections')

    if not collection_ids or 'Select' in collection_ids:
        other_collection, created = Collection.objects.get_or_create(
            title='other'
        )

        product.collections.set([other_collection])

    else:
        collections = Collection.objects.filter(
            id__in=collection_ids
        )

        product.collections.set(collections)

    return redirect('dashboard')

from django.http import JsonResponse

# Category Products
def category_products(req, id):
    products = Product.objects.filter(category_id=id)

    data = []

    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'sales': product.sales,
            'image': product.image.url if product.image else None,
        })

    return JsonResponse({
        'products': data
    })
    
# New Category in categoy section
@require_POST
def add_product_to_category(req):
    new_category = req.POST.get('category-name')
    product_ids = req.POST.getlist('category-add-products')

    category, created = Category.objects.get_or_create(name=new_category)   
    if product_ids:
        for product_id in product_ids:
            product = Product.objects.get(id=product_id)
            product.category = category
            product.save()

    return redirect('dashboard')
 
#  Delete Category in category section       
def category_delete(req, id):
    category = get_object_or_404(Category, id=id)
    other = Category.objects.get(name='other')

    Product.objects.filter(category=category).update(category=other)

    category.delete()
    return HttpResponse(status=204)  # Return a 204 No Content response to indicate success without content

# New Collection Products
@require_GET
def collection_products(req, id):
    collection = Collection.objects.get(id=id)

    products = collection.product_set.all()

    data = []

    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'sales': product.sales,
            'image': product.image.url if product.image else '',
        })

    return JsonResponse({
        'products': data
    })

# Delete Collection    
def delete_collection(req, id):
    collection = Collection.objects.get(id=id)
    collection.delete()

    return HttpResponse(status=204)  # Return a 204 No Content response to indicate success without content
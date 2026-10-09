from django.shortcuts import render,redirect, get_object_or_404
from product.models import Category,Product,Collection,Hero
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
from product.models import Order
# Create your views here

# Dashboard
@login_required
def dashboard(req):
    if req.user.is_staff:
        category = Category.objects.all()
        product = Product.objects.all()
        collection = Collection.objects.all()
        hero = Hero.objects.first()

        orders = Order.objects.select_related(
            "user"
        ).prefetch_related(
            "items__product"
        ).order_by("-created_at")

        return render(req, "dashboard.html", {
            "Products": product,
            "Categories": category,
            "Collections": collection,
            "Hero": hero,
            "orders": orders,
        })

    return redirect("home")

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
        

# Add Collections in product form
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


# Show products in category section
@require_GET
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

# Show products in collection section
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

# Creating new collection in collection section
@require_POST
def add_product_to_collection(request):
    collection_name = request.POST.get("collection-name")
    product_ids = request.POST.getlist("collection-add-products")

    collection, created = Collection.objects.get_or_create(
        title=collection_name
    )

    products = Product.objects.filter(id__in=product_ids)

    for product in products:
        product.collections.add(collection)

    return redirect("dashboard")

# Hero Delete 
def hero_delete(req):
    hero = Hero.objects.first()
    if hero:
        hero.image.delete()
        hero.delete()
    return redirect('dashboard')

# Hero Check 
def hero_check(req):
    hero = Hero.objects.first()
    if hero:
        return JsonResponse({'exists':True})
    else:
        return JsonResponse({'exists':False})

# Adding new hero
@require_POST
def add_hero(request):

    title = request.POST.get("title")
    subtitle = request.POST.get("subtitle")
    discount = request.POST.get("discount")
    product_id = request.POST.get("products")
    bg_color = request.POST.get("bg_color")
    font_btn_color = request.POST.get("font_btn_color")

    image = request.FILES.get("image")

    # Check discount
    if discount == "":
        discount = 0

    # Check colors
    if bg_color == "":
        bg_color = "#FFB86A"

    if font_btn_color == "":
        font_btn_color = "#FF6900"

    product = Product.objects.get(id=product_id)

    Hero.objects.create(
        title=title,
        subtitle=subtitle,
        image=image,
        discount=discount,
        products=product,
        bg_color=bg_color,
        font_btn_color=font_btn_color,
    )

    return redirect("dashboard")

def get_hero(request):
    hero = Hero.objects.first()

    return JsonResponse({
        'title': hero.title,
        'subtitle': hero.subtitle,
        'discount': hero.discount,
        'product_id': hero.products.id if hero.products else '',
        'bg_clr': hero.bg_color,
        'fnt_btn_color': hero.font_btn_color,
    })

# Hero Update 
@require_POST
def update_hero(request):
    hero = Hero.objects.first()

    hero.title = request.POST.get('title')
    hero.subtitle = request.POST.get('subtitle')
    hero.discount = request.POST.get('discount') or None

    product_id = request.POST.get('products')

    if product_id:
        hero.products = Product.objects.get(id=product_id)
    else:
        hero.products = None

    hero.bg_color = request.POST.get('bg_color')
    hero.font_btn_color = request.POST.get('font_btn_color')

    # New image only if user selected one
    if request.FILES.get('image'):
        hero.image = request.FILES['image']

    hero.save()

    return redirect('dashboard')

def is_admin(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_admin)
@require_POST
def update_order_status(request, order_id):

    with transaction.atomic():
        order = get_object_or_404(
            Order.objects.select_for_update(),
            id=order_id
        )

        new_status = request.POST.get("status")
        valid_statuses = dict(Order.STATUS_CHOICES)

        if new_status not in valid_statuses:
            messages.error(request, "Invalid order status.")
            return redirect("dashboard")

        if order.status in ["cancelled", "delivered"]:
            messages.error(
                request,
                "Cancelled or delivered orders cannot be changed."
            )
            return redirect("dashboard")

        order.status = new_status
        order.save(update_fields=["status"])

    messages.success(
        request,
        f"Order #{order.id} status updated successfully."
    )

    return redirect("dashboard")

@login_required
@user_passes_test(is_admin)
@require_POST
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Stock restore sirf un orders ka karo
    # jinka stock pehle deduct hua tha.
    if order.status == "pending":
        with transaction.atomic():
            order = get_object_or_404(
                Order.objects.select_for_update(),
                id=order_id
            )

            for item in order.items.all():
                product = Product.objects.select_for_update().get(
                    id=item.product_id
                )
                product.stock += item.quantity
                product.sales = max(
                    0, (product.sales or 0) - item.quantity
                )
                product.save(update_fields=["stock", "sales"])

            order.delete()

    else:
        order.delete()

    messages.success(request, f"Order #{order_id} deleted.")
    return redirect("dashboard")
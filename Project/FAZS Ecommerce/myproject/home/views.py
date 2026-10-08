from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from product.models import Product, Category, Collection, Hero, Cart, CartItem, Product, Order,OrderItem
from django.db.models import Case, When, IntegerField
from django.contrib.auth.decorators import login_required


# =========================
# HOME
# =========================

def home(req):

    products = Product.objects.all()

    categories = Category.objects.annotate(
        other_last=Case(
            When(
                name__iexact="other",
                then=1
            ),
            default=0,
            output_field=IntegerField(),
        )
    ).order_by(
        "other_last",
        "name"
    )

    collections = Collection.objects.exclude(
        title__iexact="other"
    ).order_by("title")

    hero = Hero.objects.first()

    return render(req, 'home.html', {
        'products': products,
        'Categories': categories,
        'Collections': collections,
        'hero': hero
    })


# =========================
# SEARCH
# =========================

def search(req):

    name = req.GET.get('q')

    return HttpResponse(f"Search {name}")


# =========================
# CATEGORY PRODUCTS
# =========================

def category_products(req, category_slug):

    category = get_object_or_404(
        Category,
        slug=category_slug
    )

    products = Product.objects.filter(
        category=category
    )

    return render(
        req,
        'components/category_products.html',
        {
            'category': category,
            'products': products
        }
    )


# =========================
# PRODUCT DETAIL
# =========================

def product_detail(req, product_slug):

    product = get_object_or_404(
        Product,
        slug=product_slug
    )

    category_products = Product.objects.filter(
        category=product.category
    ).exclude(
        id=product.id
    )

    collection_products = Product.objects.filter(
        collections__in=product.collections.all()
    ).exclude(
        id=product.id
    ).distinct()

    return render(
        req,
        'components/product_detail.html',
        {
            'product': product,
            'category_products': category_products,
            'collection_products': collection_products,
        }
    )


# =========================
# ADD TO CART
# =========================

@login_required
def add_to_cart(request, product_id):

    if request.method != "POST":
        return redirect("home")

    product = get_object_or_404(
        Product,
        id=product_id
    )

    quantity = int(
        request.POST.get("quantity", 1)
    )

    # Quantity valid honi chahiye
    if quantity < 1:
        return redirect(
            "product-detail",
            product.slug
        )

    # Requested quantity stock se zyada na ho
    if quantity > product.stock:
        return redirect(
            "product-detail",
            product.slug
        )

    # User ka cart lo, agar nahi hai to create karo
    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    # Check karo product pehle se cart mein hai ya nahi
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if created:

        # Product pehli dafa cart mein add ho raha hai
        cart_item.quantity = quantity

    else:

        # Product already cart mein hai
        new_quantity = cart_item.quantity + quantity

        # Existing + new quantity stock se zyada nahi honi chahiye
        if new_quantity > product.stock:
            return redirect(
                "product-detail",
                product.slug
            )

        cart_item.quantity = new_quantity

    cart_item.save()

    return redirect(
        "product-detail",
        product.slug
    )
    
# =========================
# CART VIEW
@login_required
def cart(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = cart.items.all()

    cart_total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    return render(
        request,
        'components/cart.html',
        {
            'cart_items': cart_items,
            'cart_total': cart_total
        }
    )
    
@login_required
def update_cart(request, item_id, action):

    cart_item = get_object_or_404(
    CartItem,
    id=item_id,
    cart__user=request.user
    )

    product = cart_item.product

    if action == "increase":

        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()

    elif action == "decrease":

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect("cart")

# =========================
# BUY NOW
# =========================

@login_required
def buy_now(request, product_id):

    if request.method != "POST":
        return redirect("home")

    product = get_object_or_404(
        Product,
        id=product_id
    )

    quantity = int(
        request.POST.get("quantity", 1)
    )

    if quantity < 1:
        return redirect(
            "product-detail",
            product.slug
        )

    if quantity > product.stock:
        return redirect(
            "product-detail",
            product.slug
        )

    total = product.price * quantity

    return render(
        request,
        "components/checkout.html",
        {
            "product": product,
            "quantity": quantity,
            "total": total,
        }
    )

@login_required
def place_order(request, product_id):

    if request.method != "POST":
        return redirect("home")

    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get("quantity", 1))

    if quantity < 1:
        return redirect("product-detail", product.slug)

    if quantity > product.stock:
        return redirect("product-detail", product.slug)

    total = product.price * quantity

    with transaction.atomic():

        order = Order.objects.create(
            user=request.user,
            total_amount=total
        )

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )

        product.stock -= quantity
        product.sales += quantity
        product.save()

    return render(request, "components/order_success.html", {
        "order": order
    })
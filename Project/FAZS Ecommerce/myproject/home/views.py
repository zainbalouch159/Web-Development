from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import transaction
from django.views.decorators.http import require_POST
from django.db.models import Case, When, IntegerField
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import (
    Product,
    Category,
    Collection,
    Hero,
    Cart,
    CartItem,
    Order,
    OrderItem,
)


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
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related("product")

    cart_total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    return render(request, "components/cart.html", {
        "cart_items": cart_items,
        "cart_total": cart_total,
    })
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

    product = get_object_or_404(Product, id=product_id)

    try:
        quantity = int(request.POST.get("quantity", 1))
    except (ValueError, TypeError):
        return redirect("product-detail", product.slug)

    if quantity < 1 or quantity > product.stock:
        return redirect("product-detail", product.slug)

    total = product.price * quantity

    return render(request, "components/checkout.html", {
        "product": product,
        "quantity": quantity,
        "total": total,
    })
    
    
@login_required
def place_order(request, product_id):

    if request.method != "POST":
        return redirect("home")

    try:
        quantity = int(request.POST.get("quantity", 1))
    except (ValueError, TypeError):
        return redirect("home")

    if quantity < 1:
        return redirect("home")

    with transaction.atomic():

        product = get_object_or_404(
            Product.objects.select_for_update(),
            id=product_id
        )

        if quantity > product.stock:
            return redirect("product-detail", product.slug)

        total = product.price * quantity

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
        product.sales = (product.sales or 0) + quantity
        product.save()

        quantity = request.POST.get("quantity", "1")
        print("Received quantity:", quantity)
    return redirect("order-success", order_id=order.id)

@login_required
def order_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        "components/order_success.html",
        {"order": order}
    )
    
@login_required
def cart_checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.select_related("product")

    cart_total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    return render(request, "components/cart_checkout.html", {
        "cart_items": cart_items,
        "cart_total": cart_total,
    })
    

@login_required
def place_cart_order(request):

    if request.method != "POST":
        return redirect("cart")

    with transaction.atomic():

        cart = get_object_or_404(
            Cart.objects.select_for_update(),
            user=request.user
        )

        cart_items = list(
            cart.items.select_related("product")
        )

        if not cart_items:
            return redirect("cart")

        # Har product ka stock check karo
        for item in cart_items:
            product = Product.objects.select_for_update().get(
                id=item.product_id
            )

            if item.quantity < 1 or item.quantity > product.stock:
                return redirect("cart")

        # Grand total calculate karo
        total = sum(
            item.product.price * item.quantity
            for item in cart_items
        )

        # Order create karo
        order = Order.objects.create(
            user=request.user,
            total_amount=total
        )

        # Har cart item ko order item banao
        for item in cart_items:
            product = Product.objects.select_for_update().get(
                id=item.product_id
            )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item.quantity,
                price=product.price
            )

            product.stock -= item.quantity
            product.sales = (product.sales or 0) + item.quantity
            product.save()

        # Order place hone ke baad cart empty karo
        cart.items.all().delete()

    return redirect("order-success", order_id=order.id)

@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "components/my_orders.html",
        {"orders": orders}
    )

@login_required
@require_POST
def cancel_order(request, order_id):

    with transaction.atomic():

        order = get_object_or_404(
            Order.objects.select_for_update(),
            id=order_id,
            user=request.user
        )

        # Sirf pending order cancel hoga
        if order.status != "pending":
            messages.error(
                request,
                "Only pending orders can be cancelled."
            )
            return redirect("my-orders")

        # Cancel hone par stock wapas add karo
        for item in order.items.all():

            product = Product.objects.select_for_update().get(
                id=item.product_id
            )

            product.stock += item.quantity
            product.sales = max(
                0, (product.sales or 0) - item.quantity
            )
            product.save(update_fields=["stock", "sales"])

        order.status = "cancelled"
        order.save(update_fields=["status"])

    messages.success(request, "Your order has been cancelled successfully.")
    return redirect("my-orders")
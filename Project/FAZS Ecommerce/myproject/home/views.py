from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.views.decorators.http import require_POST
from django.db.models import Case, When, IntegerField, Prefetch
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

    products = Product.objects.select_related("category")

    categories = Category.objects.prefetch_related("product_set").annotate(
        other_last=Case(
            When(name__iexact="other", then=1),
            default=0,
            output_field=IntegerField(),
        )
    ).order_by("other_last", "name")

    collections = Collection.objects.exclude(
        title__iexact="other"
    ).prefetch_related(
        Prefetch(
            "product_set",
            queryset=Product.objects.select_related("category"),
        )
    ).order_by("title")

    hero = Hero.objects.select_related("products").first()

    return render(req, "home.html", {
        "products": products,
        "Categories": categories,
        "Collections": collections,
        "hero": hero,
    })


# =========================
# SEARCH
# =========================

def search(req):
    name = req.GET.get("q", "").strip()

    products = (
        Product.objects.filter(name__icontains=name)
        if name
        else Product.objects.none()
    )

    return render(req, "components/search_results.html", {
        "products": products,
        "query": name,
    })


# =========================
# CATEGORY PRODUCTS
# =========================

def category_products(req, category_slug):

    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    return render(req, "components/category_products.html", {
        "category": category,
        "products": products,
    })


# =========================
# PRODUCT DETAIL
# =========================

def product_detail(req, product_slug):

    product = get_object_or_404(
        Product.objects.select_related("category"),
        slug=product_slug,
    )

    category_products = Product.objects.none()
    if product.category:
        category_products = Product.objects.filter(
            category=product.category
        ).exclude(id=product.id)

    collection_products = Product.objects.filter(
        collections__in=product.collections.all()
    ).exclude(id=product.id).distinct()

    return render(req, "components/product_detail.html", {
        "product": product,
        "category_products": category_products,
        "collection_products": collection_products,
    })


# =========================
# ADD TO CART
# =========================

@login_required
def add_to_cart(request, product_id):

    if request.method != "POST":
        return redirect("home")

    product = get_object_or_404(Product, id=product_id)

    try:
        quantity = int(request.POST.get("quantity", 1))
    except (ValueError, TypeError):
        messages.error(request, "Invalid quantity.")
        return redirect("product-detail", product.slug)

    if quantity < 1 or quantity > product.stock:
        messages.error(request, "Requested quantity is not available.")
        return redirect("product-detail", product.slug)

    cart, _ = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={"quantity": quantity},
    )

    if not created:
        new_quantity = cart_item.quantity + quantity

        if new_quantity > product.stock:
            messages.error(
                request,
                "You already have the maximum available quantity in your cart.",
            )
            return redirect("product-detail", product.slug)

        cart_item.quantity = new_quantity
        cart_item.save(update_fields=["quantity"])

    messages.success(request, f"{product.name} added to cart.")
    return redirect("product-detail", product.slug)


# =========================
# CART VIEW
# =========================

@login_required
def cart(request):

    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related("product")

    cart_total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    return render(request, "components/cart.html", {
        "cart_items": cart_items,
        "cart_total": cart_total,
    })


# =========================
# UPDATE CART
# =========================

@login_required
@require_POST
def update_cart(request, item_id, action):

    cart_item = get_object_or_404(
        CartItem.objects.select_related("product"),
        id=item_id,
        cart__user=request.user,
    )

    product = cart_item.product

    if action == "increase":
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save(update_fields=["quantity"])
        else:
            messages.error(request, f"Only {product.stock} in stock.")

    elif action == "decrease":
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save(update_fields=["quantity"])
        else:
            cart_item.delete()

    elif action == "remove":
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
        messages.error(request, "Invalid quantity.")
        return redirect("product-detail", product.slug)

    if quantity < 1 or quantity > product.stock:
        messages.error(request, "Requested quantity is not available.")
        return redirect("product-detail", product.slug)

    total = product.price * quantity

    return render(request, "components/checkout.html", {
        "product": product,
        "quantity": quantity,
        "total": total,
    })


# =========================
# PLACE ORDER (BUY NOW)
# =========================

@login_required
def place_order(request, product_id):

    if request.method != "POST":
        return redirect("home")

    try:
        quantity = int(request.POST.get("quantity", 1))
    except (ValueError, TypeError):
        messages.error(request, "Invalid quantity.")
        return redirect("home")

    if quantity < 1:
        messages.error(request, "Invalid quantity.")
        return redirect("home")

    with transaction.atomic():

        product = get_object_or_404(
            Product.objects.select_for_update(),
            id=product_id,
        )

        if quantity > product.stock:
            messages.error(request, f"Not enough stock for {product.name}.")
            return redirect("product-detail", product.slug)

        total = product.price * quantity

        order = Order.objects.create(
            user=request.user,
            total_amount=total,
        )

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price,
        )

        product.stock -= quantity
        product.sales = (product.sales or 0) + quantity
        product.save(update_fields=["stock", "sales"])

    return redirect("order-success", order_id=order.id)


# =========================
# ORDER SUCCESS
# =========================

@login_required
def order_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user,
    )

    return render(request, "components/order_success.html", {
        "order": order,
    })


# =========================
# CART CHECKOUT
# =========================

@login_required
def cart_checkout(request):

    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = list(cart.items.select_related("product"))

    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect("cart")

    cart_total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    return render(request, "components/cart_checkout.html", {
        "cart_items": cart_items,
        "cart_total": cart_total,
    })


# =========================
# PLACE CART ORDER
# =========================

@login_required
@require_POST
def place_cart_order(request):

    with transaction.atomic():

        cart = get_object_or_404(
            Cart.objects.select_for_update(),
            user=request.user,
        )

        cart_items = list(cart.items.all())

        if not cart_items:
            return redirect("cart")

        products = {
            p.id: p
            for p in Product.objects.select_for_update().filter(
                id__in=[item.product_id for item in cart_items]
            )
        }

        total = 0

        for item in cart_items:
            product = products[item.product_id]

            if item.quantity < 1 or item.quantity > product.stock:
                messages.error(request, f"Not enough stock for {product.name}.")
                return redirect("cart")

            total += product.price * item.quantity

        order = Order.objects.create(
            user=request.user,
            total_amount=total,
        )

        for item in cart_items:
            product = products[item.product_id]

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item.quantity,
                price=product.price,
            )

            product.stock -= item.quantity
            product.sales = (product.sales or 0) + item.quantity
            product.save(update_fields=["stock", "sales"])

        cart.items.all().delete()

    return redirect("order-success", order_id=order.id)


# =========================
# MY ORDERS
# =========================

@login_required
def my_orders(request):

    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related("items__product")
        .order_by("-created_at")
    )

    return render(request, "components/my_orders.html", {
        "orders": orders,
    })


# =========================
# CANCEL ORDER
# =========================

@login_required
@require_POST
def cancel_order(request, order_id):

    with transaction.atomic():

        order = get_object_or_404(
            Order.objects.select_for_update(),
            id=order_id,
            user=request.user,
        )

        if order.status != "pending":
            messages.error(request, "Only pending orders can be cancelled.")
            return redirect("my-orders")

        for item in order.items.all():

            if item.product_id is None:
                continue

            product = Product.objects.select_for_update().get(
                id=item.product_id
            )

            product.stock += item.quantity
            product.sales = max(0, (product.sales or 0) - item.quantity)
            product.save(update_fields=["stock", "sales"])

        order.status = "cancelled"
        order.save(update_fields=["status"])

    messages.success(request, "Your order has been cancelled successfully.")
    return redirect("my-orders")
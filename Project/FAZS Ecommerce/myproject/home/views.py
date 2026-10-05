from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from product.models import Product, Category, Collection, Hero
from django.db.models import Count, Case, When, IntegerField


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

    # Current product ki category ke products
    category_products = Product.objects.filter(
        category=product.category
    ).exclude(
        id=product.id
    )

    # Current product ki collections ke products
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
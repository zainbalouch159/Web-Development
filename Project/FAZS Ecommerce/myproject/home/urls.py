from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('search/', views.search, name='search'),
    path('category/<slug:category_slug>/', views.category_products, name='category-products'),
    path('product/<slug:product_slug>/', views.product_detail, name='product-detail'),
]
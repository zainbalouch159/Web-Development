from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('search/', views.search, name='search'),
    path('category/<slug:category_slug>/', views.category_products, name='category-products'),
    path('product/<slug:product_slug>/', views.product_detail, name='product-detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
    path('update-cart/<int:item_id>/<str:action>/', views.update_cart, name='update-cart'),
    path('buy-now/<int:product_id>/', views.buy_now, name='buy-now'),
    path('place-order/<int:product_id>/', views.place_order, name='place-order'),
]
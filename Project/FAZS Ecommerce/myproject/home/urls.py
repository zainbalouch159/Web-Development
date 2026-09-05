from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('navbar/',views.navbar),
    path('search/',views.search, name="search"),
    path('product/',views.product, name="product"),
    path('contact/',views.contact, name="contact"),
]
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.dashboard,name='dashboard'),
   path('add_product',views.add_product,name='add_product'),
    
]
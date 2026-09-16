from django.urls import path
from . import views
urlpatterns = [
   path('',views.dashboard,name='dashboard'),
   path('add_product',views.add_product,name='add_product'),
   path('add_category',views.add_category,name='add_category'),
   path('add_Collections',views.add_Collections,name='add_Collections'),
   path('product_delete/<int:id>/',views.product_delete,name='product_delete'),
   path('product_edit/<int:id>/',views.product_edit,name='product_edit'),
     
]
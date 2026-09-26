from django.urls import path
from . import views
urlpatterns = [
   path('',views.dashboard,name='dashboard'),
   path('add_product',views.add_product,name='add_product'),
   path('add_category',views.add_category,name='add_category'),
   path('add_Collections',views.add_Collections,name='add_Collections'),
   path('product_delete/<int:id>/',views.product_delete,name='product_delete'),
   path('product_edit/<int:id>/',views.product_edit,name='product_edit'),  
   path('update_product/',views.update_product,name='update_product'),  
   path('category_products/<int:id>/',views.category_products,name='category_products'),
   path('add_product_to_category/',views.add_product_to_category,name='add_product_to_category'),
   path('category_delete/<int:id>/',views.category_delete,name='category_delete'),
   path('collection_products/<int:id>/',views.collection_products,name='collection_products'),
   path('delete_collection/<int:id>/',views.delete_collection,name='delete_collection'),
   path('add_product_to_collection/',views.add_product_to_collection,name='add_product_to_collection'),
]     
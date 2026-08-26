from .views import indexview,aboutview
from django.urls import path
urlpatterns=[
 path("",indexview,name="index"),
    path("about",aboutview,name="about")
    
]
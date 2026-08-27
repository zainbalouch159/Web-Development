from .views import indexview,aboutview,detail_save
from django.urls import path
urlpatterns=[
 path("",indexview,name="index"),
    path("about",aboutview,name="about"),
    path("detail-save",detail_save,name="detail_save")
]
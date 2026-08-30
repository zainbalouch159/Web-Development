from .views import indexview,aboutview,detail_save,deleteview,edit_page
from django.urls import path
urlpatterns=[
 path("",indexview,name="index"),
    path("about",aboutview,name="about"),
    path("detail-save",detail_save,name="detail_save"),
    path("delete-view/<int:id>",deleteview,name="deleteview"),
    path('edit_page/<int:id>',edit_page, name="edit page")
]
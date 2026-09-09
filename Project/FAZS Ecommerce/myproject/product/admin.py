from django.contrib import admin
from .models import Product,Category,Collection,Hero
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Hero)
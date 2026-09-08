from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField()
    Category = models.ForeignKey()
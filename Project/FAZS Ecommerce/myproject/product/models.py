from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Collection(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField()
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT,default=1)
    collection =models.ManyToManyField(Collections)
    def __str__(self):
        return self.name

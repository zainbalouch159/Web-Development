from django.db import models
from django.core.validators import MinValueValidator

#] Create your models here.
 
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
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    sales= models.IntegerField(validators=[MinValueValidator(0)],default=0,null=True)  
    image = models.ImageField(blank=True)
    discount = models.IntegerField(validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    info = models.TextField(blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT,default=1,blank=True)
    collections =models.ManyToManyField(Collection,blank=True)
    def __str__(self):
        return self.name
 
class Hero(models.Model):
    title = models.CharField(max_length=100,blank=True)
    subtitle = models.CharField(max_length=300,blank=True)
    image = models.ImageField(blank=True)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
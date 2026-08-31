from django.db import models

# Create your models here.
class Note(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    Created_AT = models.DateField(auto_now=True)
    isPublish = models.BooleanField(default=True)
    
def __str__(self):
    return self.Title
from operator import mod
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from unicodedata import category
from django.contrib.auth.models import User
from django.db import models

'''Notes: 
>> on_delete = models.CASCADE... if object is deleted then delete all related items 
'''

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ('name',)    #tuple requires commma
        verbose_name_plural = 'Categories'  #ensures proper grammar for >1 item of this type
    
    def __str__(self):   #override default string return and use ours (each object will use its assigned name)
        return self.name

class Item(models.Model): 
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE) #get all items for this category 
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)    #blank=...allow empty field
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)    #related_name=...get items from a given user

    def __str__(self):   #override default string return and use ours (each object will use its assigned name)
        return self.name
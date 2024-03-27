from django.contrib import admin

from .models import Category, Item

# Register your models here.
"first import model, then register below"
admin.site.register(Category)
admin.site.register(Item)
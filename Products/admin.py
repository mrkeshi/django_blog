from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['categories', 'author']
    list_display = ['title','categories']


admin.site.register(models.Products, ProductAdmin)
admin.site.register(models.ProductCategories)
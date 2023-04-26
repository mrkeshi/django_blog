from django.contrib import admin
from . import  models
# Register your models here.
class Contact(admin.ModelAdmin):
    list_filter = ['name', 'email']
    list_display = ['name', 'email', 'website']


admin.site.register(models.ContactUs, Contact)
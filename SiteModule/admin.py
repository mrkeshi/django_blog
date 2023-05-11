from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models


# Register your models here.

class SettingAdmin(admin.ModelAdmin):

    list_display = ['titleSite', 'description','email','telephone','logo']


admin.site.register(models.Settings, SettingAdmin)

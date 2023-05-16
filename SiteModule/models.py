from django.db import models


# Create your models here.
class Settings(models.Model):
    titleSite = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to="setting")
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    telephone = models.CharField(max_length=30, null=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    googleplus = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    pintereset = models.CharField(max_length=100, null=True, blank=True)

# expand more..

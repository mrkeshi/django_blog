from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    email = models.EmailField(max_length=50, verbose_name="email address")
    website = models.URLField(null=True, blank=True, verbose_name="website url")
    message = models.TextField(verbose_name="text message")
    def __str__(self):
        return self.name + " | " + self.email
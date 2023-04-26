from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class ProductCategories(models.Model):
    class Meta:
        verbose_name = "product category"
        verbose_name_plural = "product categories"
    title = models.CharField(max_length=50, verbose_name="title categories")
    slug = models.SlugField(unique=True, verbose_name="url categories",null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProductCategories, self).save(args, kwargs)


class Products(models.Model):
    class Meta:
        verbose_name = "product "
        verbose_name_plural = "products"

    title = models.CharField(max_length=50, verbose_name="title")
    short_description = models.TextField(verbose_name="short description")
    content = RichTextField(blank=True, null=True)
    slug = models.SlugField(verbose_name="slug",unique=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="created_date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="author")
    categories = models.ManyToManyField(ProductCategories, verbose_name="categories", blank=True)
    image = models.ImageField(upload_to='Articles', null=True, blank=True)
    keyword = models.CharField(blank=True, null=True, max_length=150)
    price=models.BigIntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Products, self).save(args, kwargs)

    def get_absolute_url(self):
        return reverse('SingleProduct', args=[str(self.slug)])
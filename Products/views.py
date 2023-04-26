from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from Products.models import Products


class ProductsView(ListView):
    model = Products
    paginate_by = 2
    template_name = 'Products/ListProducts.html'
    context_object_name = 'Products'


class SingleProduct(DetailView):
    model = Products
    slug_field = 'slug'
    template_name = 'Products/SingleProduct.html'

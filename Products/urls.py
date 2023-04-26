from django.urls import path
from . import views

urlpatterns = [
    path('Products', views.ProductsView.as_view(), name="ProductsList"),
    path('<slug:slug>', views.SingleProduct.as_view(), name="SingleProduct"),

]
"""
URL configuration for octalab_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from django.conf import settings
from HomePage import views
from Products import views as Productviews
from django.conf.urls.static import static

urlpatterns = [
    # path('savePOst',views.bega),4
    path('', views.Home.as_view(), name="home"),
    path('admin', admin.site.urls),
    path('contact', include("ContactUs.urls")),
    path('Products', Productviews.ProductsView, name="ProductsList"),
    path('<slug:slug>', Productviews.SingleProduct.as_view(), name="SingleProduct"),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
import pandas as pd
import os
from Products.models import Products, ProductCategories
from octalab_website.settings import BASE_DIR


def ProductsView(request):
    # METAL_SALT
    pagemetal: int = 1
    if (request.GET.get('pagemetal')):
        pagemetal: int = request.GET.get('pagemetal')
    productsmetalsalt = Products.objects.filter(categories_id=3).order_by('-id')
    paginatorMetal = Paginator(productsmetalsalt, 20)
    productsmetalsalt = paginatorMetal.page(pagemetal)

    # HPLC SOLVENTS
    pagehplc: int = 1
    if (request.GET.get('pagehplc')):
        pagehplc: int = request.GET.get('pagehplc')
    productsHplc = Products.objects.filter(categories_id=4).order_by('-id')
    paginatorHplc = Paginator(productsHplc, 20)
    productsHplc = paginatorHplc.page(pagehplc)

    # SOLVENTS
    pagesolvent: int = 1
    if (request.GET.get('pagesolvent')):
        pagesolvent: int = request.GET.get('pagesolvent')
    productsSolvent = Products.objects.filter(categories_id=5).order_by('-id')
    paginatorsolvent = Paginator(productsSolvent, 20)
    productsSolvent = paginatorsolvent.page(pagesolvent)

    # INDICATORS
    pageindic: int = 1
    if (request.GET.get('pageindic')):
        pageindic: int = request.GET.get('pageindic')
    productsindic = Products.objects.filter(categories_id=6).order_by('-id')
    paginatorindic = Paginator(productsindic, 20)
    productsindic = paginatorsolvent.page(pageindic)

    # INDICATORS
    return render(request, 'Products/ListProducts.html', {
        'productsmetalsalt': productsmetalsalt,
        'productsHplc': productsHplc,
        'productsSolvent': productsSolvent,
        'productsindic': productsindic,

        'paginatorMetal': paginatorMetal,
        'paginatorHplc': paginatorHplc,
        'paginatorsolvent': paginatorsolvent,
        'paginatorindic': paginatorindic,

    })

    # def get_context_data(self, **kwargs):
    # excel_data_df = pd.read_excel(BASE_DIR / 'Products/octab.xlsx', sheet_name=0)
    # title = excel_data_df['PRODUCT NAME '].tolist()
    # code = excel_data_df['code'].tolist()
    # print("sas")
    # for i in range(1, len(title)):
    #     Pro = Products(title=title[i], code=code[i])
    #     Pro.save()

    #     excel_data_df = pd.read_excel(BASE_DIR / 'Products/octab.xlsx', sheet_name=1)
    #     title = excel_data_df['PRODUCT NAME '].tolist()
    #     GRADE = excel_data_df['GRADE'].tolist()
    #     packing = excel_data_df['PACKING'].tolist()
    #     for i in range(1, len(title)):
    #         Pro = Products(title=title[i], grade=GRADE[i], packing=packing[i])
    #         Pro.save()
    #
    #     excel_data_df = pd.read_excel(BASE_DIR / 'Products/octab.xlsx', sheet_name=2)
    #     title = excel_data_df['SOLVENTS'].tolist()
    #     GRADE = excel_data_df['GRADE'].tolist()
    #     for i in range(1, len(title)):
    #         Pro = Products(title=title[i], grade=GRADE[i])
    #         Pro.save()
    #
    # excel_data_df = pd.read_excel(BASE_DIR / 'Products/octab.xlsx', sheet_name=3)
    # title = excel_data_df.tolist()
    #
    # for i in range(1, len(title)):
    #     Pro = Products(title=title[i])
    #     Pro.save()


class SingleProduct(DetailView):
    model = Products
    slug_field = 'slug'
    template_name = 'Products/SingleProduct.html'

from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.views.generic import TemplateView

from Products.models import Products
from octalab_website.settings import BASE_DIR

class Home(TemplateView):
    template_name = 'HomePage/index.html'




def bega(request):
    excel_data_df = pd.read_excel(BASE_DIR / 'Products/octab.xlsx', sheet_name=0)
    title = excel_data_df['PRODUCT NAME '].tolist()
    code = excel_data_df['code'].tolist()
    for i in range(0, len(title)):
        Pro = Products(title=title[i].strip(), code=code[i],categories_id=3)
        Pro.save()

    excel_data_df = pd.read_excel(BASE_DIR / 'Products/octab.xlsx', sheet_name=1)
    title = excel_data_df['PRODUCT NAME '].tolist()
    GRADE = excel_data_df['GRADE'].tolist()
    packing = excel_data_df['PACKING'].tolist()
    for i in range(0, len(title)):
        Pro = Products(title=title[i].strip(), grade=GRADE[i], packing=packing[i],categories_id=4)
        Pro.save()

    excel_data_df = pd.read_excel(BASE_DIR / 'Products/octab.xlsx', sheet_name=2)
    title = excel_data_df['SOLVENTS'].tolist()
    GRADE = excel_data_df['GRADE'].tolist()
    for i in range(0, len(title)):
        Pro = Products(title=title[i].strip(), grade=GRADE[i],categories_id=5)
        Pro.save()
    excel_data_df = pd.read_excel(BASE_DIR / 'Products/octab.xlsx', sheet_name=3)

    title=excel_data_df['title'].tolist()
    for i in range(0, len(excel_data_df)):

        Pro = Products(title=title[i].strip(),categories_id=6)
        Pro.save()

    return  HttpResponse('hello')
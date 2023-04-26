from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from ContactUs.forms import ContactForm


class Contact(FormView):
    form_class = ContactForm
    template_name = 'ContactUs/contact.html'
    success_url = reverse_lazy('contact')

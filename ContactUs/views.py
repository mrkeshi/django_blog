from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from ContactUs.forms import ContactForm
from SiteModule.models import Settings
from utils.Email_Service import Email


class Contact(FormView):
    form_class = ContactForm
    template_name = 'ContactUs/contact.html'
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        data = super(Contact, self).get_context_data()
        data['info'] = Settings.objects.first()
        return data

    def form_valid(self, form):
        super(Contact, self).form_valid(form)
        messages.success(self.request, "Your request has been successfully sent")
        Email(form.cleaned_data.get('name'), form.cleaned_data.get('email'), {
            'email': form.cleaned_data.get('name'),
            'text': form.cleaned_data.get('content')
        }, 'layout/sendemail.html')
        return redirect(reverse_lazy('contact'))

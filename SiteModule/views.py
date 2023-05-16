from django.shortcuts import render

# Create your views here.
from SiteModule.models import Settings


def daynamicHeader(request):
    return render(request, 'layout/includes/header.html', {
        'info': Settings.objects.first()
    })
def daynamicFooter(request):
    return render(request,'layout/includes/footer.html',{
        'info':Settings.objects.first()
    })
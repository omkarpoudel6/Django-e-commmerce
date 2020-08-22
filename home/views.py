from django.http import HttpResponse
from django.shortcuts import render
from home.models import Setting
from home.forms import ContactForm

# Create your views here.
def index(request):
    setting=Setting.objects.get(pk=1)
    context={
        'setting':setting,
        'page':'home'
    }
    return render(request,'index.html',context)

def AboutUs(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting
    }
    return render(request,'about.html',context)

def ContactUs(request):
    contactform=ContactForm()
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
        'form':contactform
    }
    return render(request, 'contactus.html', context)

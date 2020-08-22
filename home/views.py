from django.http import HttpResponse
from django.shortcuts import render
from home.models import Setting

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
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting
    }
    return render(request, 'contactus.html', context)

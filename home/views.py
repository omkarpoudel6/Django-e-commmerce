from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting,ContactMessage
from product.models import Category,Product
from home.forms import ContactForm

# Create your views here.
def index(request):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    products_slider=Product.objects.all().order_by('id')[:5]#for slider
    latest_products=Product.objects.all().order_by('-id')[:4]#latest products
    random_products=Product.objects.all().order_by('?')[:4]#random products
    context={
        'setting':setting,
        'page':'home',
        'category':category,
        'products_slider':products_slider,
        'latest_products':latest_products,
        'random_products':random_products
    }
    return render(request,'index.html',context)


def AboutUs(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'setting':setting,
        'category':category
    }
    return render(request,'about.html',context)

def ContactUs(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            data=ContactMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Your message has been sent. Thank you for your message.')
            return HttpResponseRedirect('/contactus')
    contactform=ContactForm()
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'form':contactform,
        'category':category
    }
    return render(request, 'contactus.html', context)

def category_products(request,id,slug):
    products=Product.objects.filter(category_id=id)
    category = Category.objects.all()
    context={
        'products':products,
        'category':category
    }
    return render(request,'category_product.html',context)

def product_detail(request,id,slug):
    products=Product.objects.get(id=id)
    # context = {
    #     'product':products
    # }
    return HttpResponse(products)

def AddToCart(request,id):
    product=Product.objects.get(id=id)
    return HttpResponse(product)

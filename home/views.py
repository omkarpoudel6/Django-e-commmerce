from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from home.models import Setting,ContactMessage
from product.models import Category,Product,Images
from home.forms import ContactForm,SearchForm
from product.models import Review
from user.models import UserProfile
import json

# Create your views here.
def index(request):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    products_slider=Product.objects.all().order_by('?')[:5]#for slider
    latest_products=Product.objects.all().order_by('-id')[:4]#latest products
    random_products=Product.objects.all().order_by('?')[:4]#random products
    context={
        'setting':setting,
        'page':'home',
        'category':category,
        'products_slider':products_slider,
        'latest_products':latest_products,
        'random_products':random_products,
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
        'category':category,
        'title':slug,
    }
    return render(request,'category_product.html',context)

def product_detail(request,id,slug):
    products=Product.objects.get(id=id)
    category=Category.objects.all()
    images=Images.objects.filter(product_id=id)
    reviews=Review.objects.filter(product_id=id,status='True').order_by('-created_at')
    context={
        'category':category,
        'product':products,
        'images':images,
        'reviews':reviews
    }
    return render(request,'product_detail.html',context)

def AddToCart(request,id):
    product=Product.objects.get(id=id)
    return HttpResponse(product)


def search(request):
    if request.method=="POST":
        print("Form submitted")
        search_form=SearchForm(request.POST)
        if search_form.is_valid():
            query=search_form.cleaned_data['query']
            catid=search_form.cleaned_data['catid']
            print(query)
            print(catid)
            if catid==0:
                products=Product.objects.filter(title__icontains=query) #SELECT * FROM Product WHERE title LIKE %query%
            else:
                products=Product.objects.filter(title__icontains=query,category_id=catid)
            category=Category.objects.all()
            context={
                'products':products,
                'category':category,
                'query':query,
            }
            return render(request,'search_product.html',context)
    return HttpResponseRedirect('/')

def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = Product.objects.filter(title__icontains=q)
        results = []
        for pl in places:
            product_json = {}
            product_json = pl.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)




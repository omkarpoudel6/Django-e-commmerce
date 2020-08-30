from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from .forms import ReviewForm
from .models import Review

# Create your views here.
def index(request):
    return HttpResponse("This is product page")

def addReview(request,id):
    url=request.META.get('HTTP_REFERER') #get last url
    if request.method=="POST":
        form=ReviewForm(request.POST)
        if form.is_valid():
            data=Review()
            data.subject=form.cleaned_data['subject']
            data.comment=form.cleaned_data['comment']
            data.rating=form.cleaned_data['rating']
            data.ip=request.META.get('REMOTE_ADDR')
            data.product_id=id
            current_user=request.user
            data.user_id=current_user.id
            data.save()
            messages.success(request,"Your Review has been sent. Thank you for your interest.")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)





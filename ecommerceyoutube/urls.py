"""ecommerceyoutube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from order.views import shopcart
from user.views import login_form,signup,logout_func,faq


urlpatterns = [
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('product/',include('product.urls')),
    path('order/',include('order.urls')),
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),

    path('aboutus',AboutUs,name="aboutus"),
    path('contactus',ContactUs,name='contactus'),
    path('category/<int:id>/<slug:slug>',category_products,name="category_products"),
    path('product/<int:id>/<slug:slug>',product_detail,name="product_detail"),
    path('addtocart/<int:id>',AddToCart,name='add_to_cart'),
    path('search/',search,name="search"),
    path('search_auto/',search_auto,name='search_auto'),
    path('admin/', admin.site.urls),
    path('shopcart/',shopcart,name='shopcart'),
    path('login/',login_form,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout_func,name='logout'),
    path('faq/',faq,name='faq')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

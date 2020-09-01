from django.urls import path
from order.views import *

urlpatterns=[
    path('addtoshopcart/<int:id>',addtoshopcart,name="addtoshopcart"),
    path('deletefromcart/<int:id>',deletefromcart,name="deletefromcart")
]
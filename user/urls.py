from django.urls import path
from user.views import *

urlpatterns=[
    path("",profile,name='profile'),
    path("update/",update_user,name='update_user'),
    path("password",change_password,name='change_password'),
    path('orders/',user_orders,name='user_orders'),
    path('ordered_products/',ordered_products,name='ordered_products'),
    path('ordered_product_detail/<int:id>/<int:oid>',ordered_product_detail,name='ordered_product_detail'),
    path('orderdetail/<int:id>/',order_detail,name='order_detail')
]
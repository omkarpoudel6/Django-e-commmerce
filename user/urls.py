from django.urls import path
from user.views import *

urlpatterns=[
    path("",profile,name='profile'),
    path("update/",update_user,name='update_user')
]
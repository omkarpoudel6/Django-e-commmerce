from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('addcomment/<int:id>',addReview,name="add_review")
]
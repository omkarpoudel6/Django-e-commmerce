from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Setting)

class SettingAdmin(admin.ModelAdmin):
    list_display=['title','updated_at','status']

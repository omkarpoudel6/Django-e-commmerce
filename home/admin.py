from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Setting)

class SettingAdmin(admin.ModelAdmin):
    list_display=['title','updated_at','status']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=['name','subject','updated_at','status']
    readonly_fields = ('name','subject','email','message','ip')
    list_filter=['status']

class FAQAdmin(admin.ModelAdmin):
    list_display=['question','answer','ordernumber','status']
    list_filter=['status']

admin.site.register(FAQ,FAQAdmin)
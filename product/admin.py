from django.contrib import admin
from .models import Category,Product

# Register your models here.
#admin.site.register(Category)
#admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','parent','status')
    prepopulated_fields = {'slug':('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category','image','price')
    prepopulated_fields = {'slug':('title',)}

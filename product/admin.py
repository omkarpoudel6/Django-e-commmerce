from django.contrib import admin
from .models import Category,Product,Images

# Register your models here.
#admin.site.register(Category)
#admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','parent','status')
    prepopulated_fields = {'slug':('title',)}

#to add images of product of same page in product model in admin page
class ProductImageInline(admin.TabularInline):
    model=Images
    extra=5

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category','image_tag','price')
    prepopulated_fields = {'slug':('title',)}
    readonly_fields = ('image_tag',)
    inlines=[ProductImageInline]

admin.site.register(Images)
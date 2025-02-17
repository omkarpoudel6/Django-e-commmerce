import admin_thumbnails
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category,Product,Images,Review,Color,Size,Variants

# Register your models here.
#admin.site.register(Category)
#admin.site.register(Product)

#@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','parent','status')
    #prepopulated_fields = {'slug':('title',)}
    list_filter=['status']

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

#to add images of product of same page in product model in admin page
@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model=Images
    readonly_fields = ('id',)
    extra=1

class ProductVariantsInline(admin.TabularInline):
    model=Variants
    readonly_fields = ('image_tag',)
    extra=1
    show_change_link = True

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display=['image','title','image_thumbnail']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category','image_tag','price')
    prepopulated_fields = {'slug':('title',)}
    readonly_fields = ('image_tag',)
    inlines=[ProductImageInline,ProductVariantsInline]
    prepopulated_fields={'slug':('title',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display=['subject','comment','status','created_at']
    list_filter=['status']
    readonly_fields = ('subject','comment','ip','user','product','rating')

class ColorAdmin(admin.ModelAdmin):
    list_display=['name','code','color_tag']

class SizeAdmin(admin.ModelAdmin):
    list_display=['name','code']

class VariantsAdmin(admin.ModelAdmin):
    list_display=['title','product','color','size','price','quantity','image_tag']

admin.site.register(Images,ImagesAdmin)
admin.site.register(Category,CategoryAdmin2)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Variants,VariantsAdmin)

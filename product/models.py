from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.html import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# Create your models here.
# Here are the models of product app
#Categry models to store all the categories available
class Category(MPTTModel):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    parent=TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by=['title']

    def __str__(self):
        full_path=[self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return ' / '.join(full_path[::-1])


#product model to store all the products available product have many to one relationship with category model
class Product(models.Model):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    price=models.FloatField()
    amount=models.IntegerField()
    minamount=models.IntegerField()
    detail=RichTextUploadingField()
    slug=models.SlugField()
    status=models.CharField(max_length=10,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    def __str__(self):
        return self.title


#model to store images  of a product
class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=True)
    image=models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title



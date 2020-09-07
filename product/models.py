from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse
from django.utils.html import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.contrib.auth.models import User

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
    slug=models.SlugField(null=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by=['title']

    def get_absolute_url(self):
        return reverse('category_detail',kwars={'slug':self.slug})

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
    slug=models.SlugField(null=False,unique=True)
    status=models.CharField(max_length=10,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    def get_absolute_url(self):
        return reverse('category_detail',kwars={'slug':self.slug})

    def averagereview(self):
        reviews=Review.objects.filter(product=self, status='True').aggregate(average=Avg('rating'))
        avg=0
        if reviews['average'] is not None:
            avg=float(reviews['average'])
        return avg

    def countreview(self):
        reviews=Review.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews['count'] is not None:
            cnt=int(reviews['count'])
        return cnt

    def __str__(self):
        return self.title


#model to store images  of a product
class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=True)
    image=models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title

#model to store review for product
class Review(models.Model):
    STATUS=(
        ('New','New'),
        ('True','True'),
        ('False','False'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50,blank=True)
    comment=models.CharField(max_length=250,blank=True)
    rating=models.IntegerField(default=1)
    ip=models.CharField(max_length=20,blank=True)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject



#from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Setting(models.Model):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    title=models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    company=models.CharField(max_length=50)
    address=models.CharField(blank=True,max_length=100)
    phone=models.CharField(blank=True,max_length=15)
    fax=models.CharField(blank=True,max_length=15)
    email=models.CharField(blank=True,max_length=50)
    smtpserver=models.CharField(blank=True,max_length=50)
    smtpemail=models.CharField(blank=True,max_length=20)
    smtppassword=models.CharField(blank=True,max_length=10)
    smtpport=models.CharField(blank=True,max_length=5)
    icon=models.ImageField(blank=True,upload_to='images/')
    facebook=models.CharField(blank=True,max_length=50)
    aboutus=RichTextUploadingField(blank=True)
    contact=RichTextUploadingField(blank=True)
    references=RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS=(
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed')
    )
    name=models.CharField(blank=False,max_length=30)
    email=models.CharField(blank=False,max_length=50)
    subject=models.CharField(blank=False,max_length=10)
    message=models.TextField(blank=False,max_length=500)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip=models.CharField(blank=False,max_length=20)
    note=models.CharField(blank=True,max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    STATUS=(
        ('True','True'),
        ('False','False'),
    )
    ordernumber=models.IntegerField()
    question=models.CharField(max_length=200)
    answer=models.TextField()
    status=models.CharField(max_length=10,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

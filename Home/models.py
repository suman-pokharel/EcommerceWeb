from distutils.command.upload import upload
from email.mime import image
from telnetlib import STATUS
from tkinter import CASCADE
from unicodedata import category, name
from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.TextField(unique=True)
       
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name=models.CharField(max_length=100)
    subcategory=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.TextField(unique=True)
       
    def __str__(self):
        return self.subcategory.name + " -- " + self.name

class SubSubCategory(models.Model):
    name=models.CharField(max_length=100)
    subsubcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    slug=models.TextField(unique=True)
       
    def __str__(self):
        return self.subsubcategory.subcategory.name + " -- " + self.subsubcategory.name + " -- " + self.name

STATUS=(('active','Active'),('','Default'))
class Slider(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to ='media')
    text=models.TextField(blank=True)
    rank=models.IntegerField()
    status=models.CharField(choices=STATUS,blank=True,max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to ='media')
    rank=models.IntegerField()

    def __str__(self):
        return self.name

LABELS=(('new','New'),('hot','Hot'),('sale','Sale'),('','default'))
STOCK=(('In stock','In Stock'),('out of stock','Out of Stock'))
class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    price=models.FloatField()
    discounted_price=models.FloatField(default=0.0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    SubCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    description=models.TextField()
    information=models.TextField()
    slug=models.TextField(unique=True)
    labels=models.CharField(choices=LABELS,max_length=200)
    stock=models.CharField(choices=STOCK,max_length=200)

    def __str__(self):
        return self.name


class Review(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    review=models.TextField(blank=True)
    date=models.CharField(max_length=100)
    slug=models.TextField()
    point=models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    Name=models.CharField(max_length=300)
    email=models.EmailField(max_length=200)
    message=models.TextField()



    def __str__(self):
      return self.Name


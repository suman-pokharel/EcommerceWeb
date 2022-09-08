from django.shortcuts import render,redirect
from email.message import Message
from itertools import count
from pickle import NONE
from urllib import request
from django import views
from django.forms import SlugField
from django.views import View
from .models import *
from django.views.generic import View
import datetime,random
from django.contrib.auth.models import User
from django.contrib import messages,auth


# Create your views here.
class Base(View):
    views = {}
    views['categories'] = Category.objects.all()
    
	
    

class HomeView(Base):
    def get(self,request):
        self.views['sliders']=Slider.objects.all()
        self.views['news']=Product.objects.filter(labels='new')
        self.views['hots']=Product.objects.filter(labels='hot')
        self.views['sales']=Product.objects.filter(labels='sale')
        return render(request, 'shop-index.html', self.views)

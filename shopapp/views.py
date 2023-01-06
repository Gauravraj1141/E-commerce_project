from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Product

import math

# Create your views here.
def index(request):
    mydata = Product.objects.all()
    n = len(mydata)
    nslides = math.ceil(n/4)
    params = {"product":mydata,"no_of_slides":nslides, "range":range(1,nslides)}
    return render(request,"shop\inew.html",params)



def aboutus(request):
    return HttpResponse("You are inside the about us")

def contactus(request):
    return HttpResponse("You are inside the contactus")

def tracker(request):
    return HttpResponse("You are inside the tracker")

def search(request):
    return HttpResponse("You are inside the search")

def productview(request):
    return HttpResponse("You are inside the productview")

def checkout(request):
    return HttpResponse("You are inside the checkout")
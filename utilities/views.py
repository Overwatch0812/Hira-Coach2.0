from django.shortcuts import render
from .models import services,gallery

# Create your views here.

def about_us(request):
    return render(request,"about.html")

def service(request):
    service=services.objects.all()
    return render(request,"service.html",{'services':service})

def feature(request):
    galleri=gallery.objects.all()
    return render(request,"feature.html",{'gallery':galleri})

def contact_us(request):
    return render(request,'contact.html')
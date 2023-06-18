from django.shortcuts import render
from utilities.models import CustomUser

# Create your views here.
def home(request):
    user=CustomUser.objects.all()
    return render(request,'index.html',{'users':user})
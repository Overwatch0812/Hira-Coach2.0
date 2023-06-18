from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


# Create your models here.
class services(models.Model):
    img=models.ImageField(upload_to='services')
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=1000)
    more_description=models.TextField()

    def __str__(self):
        return self.title

class gallery(models.Model):
    img=models.ImageField(upload_to='features')
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=1000)

    def __str__(self):
        return self.title


# Create your models here.
class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(max_length=100,unique=True)
    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]   
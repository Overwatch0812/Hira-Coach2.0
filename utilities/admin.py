 
from django.contrib import admin
from .models import CustomUser,services,gallery

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(services)
admin.site.register(gallery)

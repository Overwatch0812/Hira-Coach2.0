from django.urls import path
from . import views

urlpatterns=[
    path('about_us',views.about_us,name='about_us'),
    path('service',views.service,name='service'),
    path('feature',views.feature,name='feature'),
    path('contact_us',views.contact_us,name="contact_us")
]
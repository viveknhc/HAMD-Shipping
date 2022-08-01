from django.urls import path
from  . import views

app_name='web'

urlpatterns = [
    path('',views.index,name="index"),
    path('service',views.service,name="service"),
    path('single-service',views.servicesingle,name="single-service"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('gallery',views.gallery,name="gallery"),
]

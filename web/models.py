from distutils.command.upload import upload
from http import client
from statistics import mode
from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField

# Create your models here.
class Banner(models.Model):
    Banner_image = models.ImageField(upload_to = "banner")
    Banner_title = models.CharField(max_length=100)
    Banner_description = models.CharField(max_length=100)


class Testimonial(models.Model):
    person = models.CharField(max_length=50,verbose_name='name')
    post = models.CharField(max_length=100)
    quote = models.CharField(max_length=1000)
    person_img = models.ImageField(upload_to="testimonial",verbose_name='imag')

    def __str__(self):
        return self.person

class About(models.Model):
    vision_description = models.CharField(max_length=1000,verbose_name='vision_description')
    vision_image = models.ImageField(upload_to="about")
    mission_description = models.CharField(max_length=1000)
    mission_image = models.ImageField(upload_to="about")
    about = models.CharField(max_length=1000)
    About_img = models.ImageField(upload_to="about",verbose_name='imag')

    def __str__(self):
        return self.about

class Clients(models.Model):
    client_image = models.ImageField(upload_to="client")

class Service(models.Model):
    service_image = VersatileImageField(upload_to = "service")
    service_title = models.CharField(max_length=100)
    service_description = HTMLField()
    summery_content = models.CharField(max_length=300) 

    def __str__(self):
        return self.service_title


class Address(models.Model):
    company_name = models.CharField(max_length=50)
    company_address = models.CharField(max_length=100)
    phone_number_1 = models.CharField(max_length=20)
    phone_number_2 = models.CharField(max_length=20)
    company_email = models.EmailField()

# class OpeningHour(models.Model):
#     starting_day = models.CharField(max_length=50)
#     ending_day = models.CharField(max_length=50)
#     opening_time = models.CharField()
#     closing_time = models.CharField()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name
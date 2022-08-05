from multiprocessing import context
from django.shortcuts import get_object_or_404, render

from .models import *

def index(request):
    banner = Banner.objects.filter().order_by('-id')
    about = About.objects.all()
    testimonial = Testimonial.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['subject']
        msg = request.POST['message']
        object = Contact(name=name,email=email,subject=sub,message=msg)
        object.save()
    context = {
        "testimonial":testimonial,
        "banner":banner,
        "about":about,
        
    }
    return render(request,'web/index.html',context)

def service(request):
    service = Service.objects.all()
    context = {
        "service":service
    }
    return render(request,'web/service.html',context)

def about(request):
    about = About.objects.all()
    context = {
        "about":about
    }
    return render(request,'web/about.html',context)


def gallery(request):
    return render(request,'web/gallery.html')

def servicesingle(request,id):
    single_service= get_object_or_404(Service,id=id)
    context ={
        "single_service":single_service,

    }

    return render(request,'web/single-service.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['subject']
        msg = request.POST['message']
        object = Contact(name=name,email=email,subject=sub,message=msg)
        object.save()
    return render(request,"web/contact.html")

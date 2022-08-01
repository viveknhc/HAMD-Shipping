from django.shortcuts import render



def index(request):
    return render(request,'web/index.html')

def service(request):
    return render(request,'web/service.html')

def about(request):
    return render(request,'web/about.html')

def contact(request):
    return render(request,'web/contact.html')

def gallery(request):
    return render(request,'web/gallery.html')

def servicesingle(request):
    return render(request,'web/single-service.html')

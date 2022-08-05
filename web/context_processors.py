from .models import About, Address, Clients, Service


def main_context(request):
    clients = Clients.objects.all()
    address = Address.objects.filter().order_by('-id')
    service = Service.objects.all()
    about = About.objects.filter().order_by('-id')
    return {
        "domain": request.META["HTTP_HOST"],
        "clients":clients,
        "address":address,
        "service":service,
        "about":about,
    }
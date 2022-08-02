from .models import Clients


def main_context(request):
    clients = Clients.objects.all()
    return {
        "domain": request.META["HTTP_HOST"],
        "clients":clients,
    }
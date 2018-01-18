from .models import Enterprise, Service
from django.shortcuts import render


def index(request):
    enterprise_list = Enterprise.objects.order_by('-city_region')[:5]
    context = {'enterprise_list': enterprise_list}
    return render(request, 'business/index.html', context)

def services(request):
    services = Service.objects
    context = {'services': services}
    return render(request, 'business/services.html', context)

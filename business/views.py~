from .models import Organisation, Service, Membership, Category
from django.shortcuts import render

# For API.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from business.models import Organisation
from business.serializers import OrganizationSerializer


def index(request):
    enterprise_list = Organisation.objects.order_by('-city_region')[:5]
    context = {'enterprise_list': enterprise_list}
    return render(request, 'business/index.html', context)


def services(request):
    services = Service.objects
    context = {'services': services}
    return render(request, 'business/services.html', context)

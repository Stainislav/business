from .models import Organisation, Service, Membership
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


@api_view(['GET', 'POST'])
def organization_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        organizations = Organisation.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



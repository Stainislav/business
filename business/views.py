from .models import Organisation, Service, Membership, Category
from django.shortcuts import render

# For API.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from business.models import Organisation
from business.serializers import OrganizationSerializer
#from business.serializers import CategorySerializer


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


@api_view(['GET', 'PUT', 'DELETE'])
def organization_by_district(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        organisation = Organisation.objects.get(pk=pk)
    except Organisation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrganizationSerializer(organisation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrganizationSerializer(organisation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        organisation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
@api_view(['GET', 'PUT', 'DELETE'])
def service_by_category(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(Category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
class CategoryList(generics.ListAPIView):
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return Category.objects.filter(purchaser__username=username)

'''




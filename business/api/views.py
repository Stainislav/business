from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
    )

from rest_framework.generics import ListAPIView, RetrieveAPIView

from business.models import Organisation, Service
from .serializers import OrganisationSerializer, ServiceSerializer


class OrganisationListAPIView(ListAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'name', 'description', 'goods__name', 'membership__price', 'membership__service__category__name']
    ordering_fields = ['id', 'name', 'description', 'goods__name', 'membership__price', 'membership__service__category__name']


class OrganisationByDistrictAPIView(ListAPIView):
    serializer_class = OrganisationSerializer
  
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        district = self.kwargs['district_id']
        return Organisation.objects.filter(district__id=district)


class ServiceDetailAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'service_id'
    

class OrganisationDetailAPIView(RetrieveAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'organisation_id'


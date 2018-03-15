from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
    )

from rest_framework.generics import ListAPIView, RetrieveAPIView

from business.models import Organisation
from .serializers import OrganisationSerializer


class OrganisationListAPIView(ListAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'name', 'description', 'goods__name', 'membership__price', 'membership__service__category__name']
    ordering_fields = ['id', 'name', 'description', 'goods__name', 'membership__price', 'membership__service__category__name']

class OrganisationDetailAPIView(RetrieveAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'district'
    lookup_url_kwarg = 'district_id'

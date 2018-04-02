from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
    )

from rest_framework.generics import ListAPIView, RetrieveAPIView

from business.models import Organization, Goods
from .serializers import OrganizationSerializer, GoodsSerializer


# Выводит список предприятий.
class OrganizationListAPIView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'name', 'description', 'goods__name', 'goodspriceconnection__price', 'goodspriceconnection__goods__category__name']
    ordering_fields = ['id', 'name', 'description', 'goods__name', 'goodspriceconnection__price', 'goodspriceconnection__goods__category__name']


# Показывает список предприятий, отфильтрованных по выбранному району.
class OrganizationByDistrictAPIView(ListAPIView):
    serializer_class = OrganizationSerializer
  
    def get_queryset(self):
        
        district = self.kwargs['district_id']
        return Organization.objects.filter(district__id=district)


# Детальная информация по товару.
class GoodsDetailAPIView(RetrieveAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'goods_id'
    

# Детальная информация по предприятию.
class OrganizationDetailAPIView(RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'organization_id'


from django.conf.urls import url

from .views import (
    OrganizationListAPIView, 
    OrganizationDetailAPIView,
    GoodsDetailAPIView,
    OrganizationByDistrictAPIView
    )


urlpatterns = [
    url(r'^$', OrganizationListAPIView.as_view(), name='list'),
    url(r'^organizations/(?P<district_id>\d+)/$', OrganizationByDistrictAPIView.as_view(), name='organizations'),    
    url(r'^goods-details/(?P<goods_id>\d+)/$', GoodsDetailAPIView.as_view(), name='goods-details'),
    url(r'^organization-details/(?P<organization_id>\d+)/$', OrganizationDetailAPIView.as_view(), name='organization-details'),    
]


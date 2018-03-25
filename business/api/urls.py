from django.conf.urls import url
from django.contrib import admin

from .views import (
    OrganisationListAPIView, 
    OrganisationDetailAPIView,
    ServiceDetailAPIView,
    OrganisationByDistrictAPIView
    )


urlpatterns = [
    url(r'^$', OrganisationListAPIView.as_view(), name='list'),
    url(r'^(?P<district_id>\d+)/$', OrganisationByDistrictAPIView.as_view(), name='district'),    
    url(r'^service/(?P<service_id>\d+)/$', ServiceDetailAPIView.as_view(), name='service'),
    url(r'^details/(?P<organisation_id>\d+)/$', OrganisationDetailAPIView.as_view(), name='organisation'),    
]


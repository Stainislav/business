from django.conf.urls import url
from django.contrib import admin

from .views import (
    OrganisationListAPIView, 
    OrganisationDetailAPIView
    )


urlpatterns = [
    url(r'^$', OrganisationListAPIView.as_view(), name='list'),
    url(r'^(?P<district_id>\d+)/$', OrganisationDetailAPIView.as_view(), name='detail'),    
]  


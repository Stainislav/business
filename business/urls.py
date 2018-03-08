from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^organizations/$', views.organization_list),
    url(r'^organizations/(?P<pk>[0-9]+)/$', views.organization_by_district),    
   # url(r'^service/(?P<pk>[0-9]+)/$', views.service_by_category),
    #url(r'^organizations/(?P<pk>[0-9]+)/(?P<category>.+)/$', CategoryList.as_view()),
]


# urlpatterns = format_suffix_patterns(urlpatterns)


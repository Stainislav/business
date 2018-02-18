from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^organizations/$', views.organization_list),
    url(r'^organizations/(?P<pk>[0-9]+)/$', views.organization_by_district)
]


# urlpatterns = format_suffix_patterns(urlpatterns)


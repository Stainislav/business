from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    # url(r'^business/', include('business.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('business.api.urls')),  
]

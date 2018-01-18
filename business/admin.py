from django.contrib import admin
from .models import City_region, Category, Enterprise_network, Enterprise, Service


admin.site.register(City_region)
admin.site.register(Category)
admin.site.register(Enterprise_network)
admin.site.register(Enterprise)
admin.site.register(Service)

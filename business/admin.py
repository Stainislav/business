from django.contrib import admin
from .models import District, Category, Enterprise_network, Enterprise, Service


admin.site.register(District)
admin.site.register(Category)
admin.site.register(Enterprise_network)
admin.site.register(Enterprise)
admin.site.register(Service)

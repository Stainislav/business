from django.contrib import admin
from .models import District, Category, Enterprise_network, Organisation, Service, Membership

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Organisation


admin.site.register(District)
admin.site.register(Category)
admin.site.register(Enterprise_network)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Service)
admin.site.register(Membership)

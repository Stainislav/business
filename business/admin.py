from django.contrib import admin
from .models import District, Category, Enterprise_network, Organisation, Service, Membership

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['id', 'name', 'description']
    search_fields = ['id', 'name', 'description']

    class Meta:
        model = Organisation


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = District


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = Category


class Enterprise_networkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = Enterprise_network


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_filter = ['id', 'name', 'category']
    search_fields = ['id', 'name', 'category']

    class Meta:
        model = Service


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['id', 'organisation', 'service', 'price']
    list_filter = ['id', 'organisation', 'service', 'price']
    search_fields = ['id', 'organisation', 'service', 'price']

    class Meta:
        model = Membership


admin.site.register(District, DistrictAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Enterprise_network, Enterprise_networkAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Membership, MembershipAdmin)

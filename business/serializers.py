from rest_framework import serializers
from business.models import Organisation


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('name', 'description', 'enterprise_network', 'city_region', 'goods')




'''
from business.models import Membership

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('organisation', 'service', 'price')
'''




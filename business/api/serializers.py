from rest_framework import serializers
from business.models import Organisation
from business.models import Category

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('name', 'description', 'enterprise_network', 'city_region', 'goods')


'''
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')
'''

'''
from business.models import Membership

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('organisation', 'service', 'price')
'''




from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField

from business.models import Organisation, Service

class OrganisationSerializer(ModelSerializer):
    goods = StringRelatedField(many=True)
    district = StringRelatedField(many=True)

    class Meta:
        model = Organisation
        fields = ('id', 'name', 'description', 'organization_network', 'district', 'goods')


class ServiceSerializer(ModelSerializer):
    
    class Meta:
        model = Service
        fields = ('id', 'name', 'category')
 


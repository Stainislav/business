from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField

from business.models import Organisation

class OrganisationSerializer(ModelSerializer):
    goods = StringRelatedField(many=True)
    
    class Meta:
        model = Organisation
        fields = ('id', 'name', 'description', 'organization_network', 'district', 'goods')



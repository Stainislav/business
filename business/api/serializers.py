from rest_framework.serializers import ModelSerializer
from business.models import Organisation

class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('id', 'name', 'description', 'organization_network', 'district', 'goods')



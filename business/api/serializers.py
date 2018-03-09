from rest_framework.serializers import ModelSerializer
from business.models import Organisation

class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('id', 'name', 'description', 'enterprise_network', 'city_region', 'goods')


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




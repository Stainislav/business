from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField

from business.models import Organization, Goods


class OrganizationSerializer(ModelSerializer):
    goods = StringRelatedField(many=True)
    district = StringRelatedField(many=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'organization_network', 'district', 'goods')


class GoodsSerializer(ModelSerializer):

    class Meta:
        model = Goods
        fields = ('id', 'name', 'category')


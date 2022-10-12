from rest_framework import serializers
from enterprise.models import Enterprise, Product, Commodity


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = (
            "id",
            "title",
            "description",
            "district",
            "enterprise_network",
            "commodities",
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'

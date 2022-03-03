from rest_framework import serializers
from .ProductModel import Product

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', 
        lookup_field = 'pk')
    price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'pk',
            'name',
            'price',
            'url',
        ]

    def get_price(self, obj):
        return obj.get_price()
from rest_framework import serializers
from .ProductModel import Product

class ProductDetailSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            'name',
            'category',
            'description',
            'price',
        ]
    
    def get_price(self, obj):
        return obj.get_price()
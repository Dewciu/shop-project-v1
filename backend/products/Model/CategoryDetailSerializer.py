from rest_framework import serializers

from products.Model.CategoryModel import Category
from .ProductSerializer import ProductSerializer

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = [
            'pk',
            'name',
            'products',
        ]
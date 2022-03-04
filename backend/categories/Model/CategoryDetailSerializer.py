from rest_framework import serializers

from categories.Model.CategoryModel import Category
from products.Model.ProductSerializer import ProductSerializer

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = [
            'pk',
            'name',
            'products',
        ]
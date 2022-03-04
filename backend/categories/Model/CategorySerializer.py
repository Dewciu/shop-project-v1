from rest_framework import serializers
from categories.Model.CategoryModel import Category

class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='category-detail', 
        lookup_field = 'name')

    class Meta:
        model = Category
        fields = [
            'pk',
            'name',
            'url',
        ]
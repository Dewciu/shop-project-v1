from django.shortcuts import get_object_or_404
from rest_framework import generics
from categories.Model.CategoryModel import Category
from categories.Model.CategoryDetailSerializer import CategoryDetailSerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'name'


category_detail_view = CategoryDetailView.as_view()
            
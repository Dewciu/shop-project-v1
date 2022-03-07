from django.shortcuts import get_object_or_404
from rest_framework import generics
from categories.Model.CategoryModel import Category
from categories.Model.CategoryDetailSerializer import CategoryDetailSerializer
from rest_framework import viewsets

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'name'

# class CategoryViewSet(viewsets.ModelViewSet):
#     serializer_class = CategoryDetailSerializer
#     queryset = Category.objects.all()


category_detail_view = CategoryDetailView.as_view()
            
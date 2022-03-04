from rest_framework import generics
from categories.Model.CategorySerializer import CategorySerializer
from categories.Model.CategoryModel import Category

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

category_list_view = CategoryListView.as_view()


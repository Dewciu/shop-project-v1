from django.urls import path
from .CategoryListView import category_list_view
# from .ProductListView import category_detail_view
from .CategoryDetailView import category_detail_view
from .ProductDetailView import product_detail_view

urlpatterns = [
    path('', category_list_view, name = 'category-list'),
    path('<str:name>/products/', category_detail_view, name='category-detail'),
    path('products/<int:pk>/', product_detail_view, name='product-detail'),
]
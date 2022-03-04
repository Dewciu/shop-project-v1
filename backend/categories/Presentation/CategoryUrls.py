from django.urls import path, include
from .CategoryListView import category_list_view
from .CategoryDetailView import category_detail_view
from products.Presentation.ProductDetailView import product_detail_view

urlpatterns = [
    path('', category_list_view, name = 'category-list'),
    path('/<str:name>/product-list', category_detail_view, name='category-detail'),
]

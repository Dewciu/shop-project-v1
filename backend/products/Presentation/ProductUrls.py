from django.urls import path
from .ProductDetailView import product_detail_view

urlpatterns = [
    path('<int:pk>/details', product_detail_view, name='product-detail'),
]
from products.Model.ProductSerializer import ProductSerializer
from products.Model.ProductModel import Product
from rest_framework import generics
from products.Model.ProductDetailSerializer import ProductDetailSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'


product_detail_view = ProductDetailView.as_view()


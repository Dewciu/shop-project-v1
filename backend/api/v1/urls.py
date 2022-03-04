from django.urls import path, include

urlpatterns = [
    path('/categories', include('categories.Presentation.CategoryUrls')),
    path('/products', include('products.Presentation.ProductUrls')),
]


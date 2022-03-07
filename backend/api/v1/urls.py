from django.urls import path, include

urlpatterns = [
    path('categories/', include('categories.Presentation.CategoryUrls')),
    path('products/', include('products.Presentation.ProductUrls')),
    path('cart/', include('shopping_cart.Presentation.CartUrls')),
    path('cartitem/', include('shopping_cart.Presentation.CartItemUrls')),
]



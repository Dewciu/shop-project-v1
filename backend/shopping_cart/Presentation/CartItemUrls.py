from django.urls import path
from shopping_cart.Presentation.CartItemCreateView import cart_item_create_view
from shopping_cart.Presentation.CartItemDestroyView import cart_item_destroy_view

urlpatterns = [
    path('', cart_item_create_view),
    path('<int:pk>/delete-product', cart_item_destroy_view)
]
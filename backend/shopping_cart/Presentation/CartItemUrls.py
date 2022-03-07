from django.urls import path
from shopping_cart.Presentation.CartItemCreateView import cart_item_view

urlpatterns = [
    path('', cart_item_view),
]
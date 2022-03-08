from rest_framework import generics
from shopping_cart.Model.CartModel import Cart
from shopping_cart.Model.CartSerializer import CartSerializer


class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

cart_create_view = CartCreateView.as_view()
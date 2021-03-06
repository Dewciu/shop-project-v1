from rest_framework import mixins, generics
from shopping_cart.Model.CartModel import Cart
from shopping_cart.Model.CartSerializer import CartSerializer

class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'pk'

cart_detail_view = CartDetailView.as_view()
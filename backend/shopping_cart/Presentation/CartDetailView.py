from rest_framework import mixins, generics
from shopping_cart.Model.CartModel import Cart
from shopping_cart.Model.CartSerializer import CartSerializer

# class CartView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'pk'

cart_detail_view = CartDetailView.as_view()
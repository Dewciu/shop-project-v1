from rest_framework import generics, mixins
from shopping_cart.Model.CartItemModel import CartItem
from shopping_cart.Model.CartItemSerializer import CartItemSerializer

class CartItemView(mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    # lookup_field = 'pk'

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        cart = kwargs.get('cart')
        if cart is not None:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)
        

    # def create(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
    
cart_item_view = CartItemView.as_view()

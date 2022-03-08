from rest_framework import generics
from shopping_cart.Model.CartItemModel import CartItem
from shopping_cart.Model.CartItemSerializer import CartItemSerializer
from shopping_cart.Model.CartItemModel import CartItem


class CartItemDestroyView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        obj = CartItem.objects.get(pk = instance.pk)
        if obj.quantity > 1:
            obj.quantity = obj.quantity - 1
            obj.save()
        else:
            super().perform_destroy(instance)
    
cart_item_destroy_view = CartItemDestroyView.as_view()
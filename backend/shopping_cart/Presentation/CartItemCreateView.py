from rest_framework import generics
from shopping_cart.Model.CartItemModel import CartItem
from shopping_cart.Model.CartItemSerializer import CartItemSerializer
from shopping_cart.Model.CartItemModel import CartItem


class CartItemCreateView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            product = serializer.validated_data.get('product')
            cart = serializer.validated_data.get('cart')
            quantity = serializer.validated_data.get('quantity')
    
            product_exists = CartItem.objects.filter(product = product, cart=cart)

            if product_exists:
                
                existing_product = CartItem.objects.get(product=product, cart=cart)
                existing_product.quantity = quantity + existing_product.quantity
                print(existing_product.quantity)
                existing_product.save()
               
            else:

                serializer.save()
    
cart_item_create_view = CartItemCreateView.as_view()

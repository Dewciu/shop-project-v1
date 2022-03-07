from rest_framework import serializers
from shopping_cart.Model.CartModel import Cart
from shopping_cart.Model.CartItemSerializer import CartItemSerializer

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = [
            'pk',
            'created',
            'items',
        ]

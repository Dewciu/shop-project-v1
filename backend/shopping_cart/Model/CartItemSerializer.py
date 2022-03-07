from rest_framework import serializers
from shopping_cart.Model.CartItemModel import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    item_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CartItem
        fields = [
            'pk',
            'cart',
            'product',
            'quantity',
            'item_price',
        ]

    def get_item_price(self, obj):
        return obj.get_item_price()
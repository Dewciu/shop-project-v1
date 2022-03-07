from django.contrib import admin

from shopping_cart.Model.CartModel import Cart
from shopping_cart.Model.CartItemModel import CartItem

# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)
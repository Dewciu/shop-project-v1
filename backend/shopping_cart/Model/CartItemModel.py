from django.db import models

from products.Model.ProductModel import Product
from shopping_cart.Model.CartModel import Cart

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', null=True, blank=False, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, related_name='product', blank=False, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1, null=True, blank=False)

    def get_item_price(self):
        return self.product.get_price() * self.quantity



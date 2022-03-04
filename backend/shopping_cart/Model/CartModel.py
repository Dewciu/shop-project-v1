from django.db import models
from products.Model.ProductModel import Product

class Cart(models.Model):
    products = models.ManyToManyField(Product)
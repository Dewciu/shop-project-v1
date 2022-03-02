from django.db import models
from .CategoryModel import Category

class Product(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=3000, null=True, blank=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sale_discount = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=1)

    @property
    def price(self):
        return "%2.f" %(float(self.base_price)*float(self.sale_discount))

    def __str__(self):
        return self.name
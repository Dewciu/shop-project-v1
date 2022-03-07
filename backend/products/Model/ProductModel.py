from django.db import models
from categories.Model.CategoryModel import Category

class Product(models.Model):
    name = models.CharField(max_length=50, null=True, unique=True)
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=3000, null=True, blank=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sale_discount = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=1)

   
    def get_price(self):
        return float(self.base_price)*float(self.sale_discount)

    def __str__(self):
        return self.name
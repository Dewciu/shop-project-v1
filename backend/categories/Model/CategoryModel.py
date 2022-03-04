from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, null=True, unique=True)

    def __str__(self):
        return self.name
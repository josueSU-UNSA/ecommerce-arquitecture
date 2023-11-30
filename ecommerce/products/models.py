from django.db import models


class Category(models.Model):
    nme = models.CharField(max_length=100)


class Producto(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Treatment(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    deals = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

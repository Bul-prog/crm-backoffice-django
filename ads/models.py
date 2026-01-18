from django.db import models

from products.models import Product


class Ad(models.Model):
    name = models.CharField('Название рекламной кампании', max_length=255, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ads')
    channel = models.CharField('Канал продвижения', max_length=255)
    budget = models.DecimalField('Бюджет на рекламу', max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return self.name


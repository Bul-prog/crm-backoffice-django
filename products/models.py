from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание')
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

from django.db import models
from products.models import Product
from customers.models import Customer


class Contract(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='contract')
    document = models.FileField(upload_to='contracts/')
    signed_date = models.DateField()
    valid_until = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


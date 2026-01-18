from django.db import models
from leads.models import Lead


class Customer(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, related_name='customer')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.lead.last_name} {self.lead.first_name}'

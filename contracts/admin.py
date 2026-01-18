
from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'amount', 'signed_date')

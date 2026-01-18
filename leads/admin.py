from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'ad', 'created_at')
    search_fields = ('full_name', 'phone', 'email')

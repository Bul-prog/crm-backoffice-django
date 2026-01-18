from django.contrib import admin

from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'channel', 'budget')
    list_filter = ('channel', 'product')
    search_fields = ('name',)


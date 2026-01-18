from django.shortcuts import render

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Count, Sum, F, Value, DecimalField
from django.db.models.functions import Coalesce
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Ad


class AdListView(PermissionRequiredMixin, ListView):
    model = Ad
    template_name = 'ads/ads-list.html'
    permission_required = 'ads.view_ad'
    context_object_name = 'ads'


class AdDetailView(PermissionRequiredMixin, DetailView):
    model = Ad
    template_name = 'ads/ads-detail.html'
    permission_required = 'ads.view_ad'


class AdCreateView(PermissionRequiredMixin, CreateView):
    model = Ad
    fields = ['name', 'product', 'channel', 'budget']
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.add_ad'


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    model = Ad
    fields = ['name', 'product', 'channel', 'budget']
    template_name = 'ads/ads-edit.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.change_ad'


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    model = Ad
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.delete_ad'


class AdStatisticView(PermissionRequiredMixin, ListView):
    model = Ad
    template_name = 'ads/ads-statistic.html'
    permission_required = 'ads.view_ad'
    context_object_name = 'ads'

    def get_queryset(self):
        money_field = DecimalField(max_digits=12, decimal_places=2)

        return (
            Ad.objects
            .annotate(
                leads_count=Count('leads', distinct=True),
                customers_count=Count('leads__customer', distinct=True),
                income=Coalesce(
                    Sum('leads__customer__contract__amount'),
                    Value(0),
                    output_field=money_field,
                ),
            )
            .annotate(
                profit=F('income') - Coalesce(F('budget'), Value(0), output_field=money_field),
            )
            .order_by('name')
        )


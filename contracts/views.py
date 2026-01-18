from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Contract, Customer


class ContractListView(PermissionRequiredMixin, ListView):
    model = Contract
    template_name = 'contracts/contracts-list.html'
    permission_required = 'contracts.view_contract'
    context_object_name = 'contracts'


class ContractDetailView(PermissionRequiredMixin, DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'
    permission_required = 'contracts.view_contract'


class ContractCreateView(PermissionRequiredMixin, CreateView):
    model = Contract
    fields = ['name', 'product', 'customer', 'document', 'signed_date', 'valid_until', 'amount']
    template_name = 'contracts/contracts-create.html'
    success_url = reverse_lazy('contracts:list')
    permission_required = 'contracts.add_contract'


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    model = Contract
    fields = ['name', 'product', 'customer', 'document', 'signed_date', 'valid_until', 'amount']
    template_name = 'contracts/contracts-edit.html'
    success_url = reverse_lazy('contracts:list')
    permission_required = 'contracts.change_contract'


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:list')
    permission_required = 'contracts.delete_contract'


class ContractCreateForCustomerView(PermissionRequiredMixin, CreateView):
    model = Contract
    fields = ['name', 'product', 'document', 'signed_date', 'valid_until', 'amount']
    template_name = 'contracts/contracts-create.html'
    permission_required = 'contracts.add_contract'

    def dispatch(self, request, *args, **kwargs):
        self.customer = get_object_or_404(Customer, pk=kwargs['customer_id'])

        # OneToOne: если контракт уже существует — не создаём новый
        if hasattr(self.customer, 'contract'):
            return redirect('contracts:detail', pk=self.customer.contract.pk)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['customer'] = self.customer
        return ctx

    def form_valid(self, form):
        form.instance.customer = self.customer
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customers:detail', kwargs={'pk': self.customer.pk})
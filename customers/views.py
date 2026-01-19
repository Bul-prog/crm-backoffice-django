from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponseNotAllowed

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Customer
from leads.models import Lead


class CustomerListView(PermissionRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    permission_required = 'customers.view_customer'
    context_object_name = 'customers'


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'
    permission_required = 'customers.view_customer'


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.delete_customer'



class CustomerCreateFromLeadView(PermissionRequiredMixin, CreateView):
    model = Customer
    fields = []  # lead предзаполнен и не редактируется
    template_name = 'customers/customers-create.html'
    permission_required = 'customers.add_customer'

    def dispatch(self, request, *args, **kwargs):
        self.lead = get_object_or_404(Lead, pk=kwargs['lead_id'])

        if hasattr(self.lead, 'customer'):
            return redirect('customers:detail', pk=self.lead.customer.pk)

        request.session['lead_id_for_customer_create'] = self.lead.pk
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['lead'] = self.lead  # если шаблон показывает lead — будет ок
        return ctx

    def form_valid(self, form):
        form.instance.lead = self.lead
        return super().form_valid(form)

    def get_success_url(self):
        # сразу после создания ведём на создание контракта для клиента
        return reverse('contracts:create_for_customer', kwargs={'customer_id': self.object.pk})



class CustomerCreatePostView(PermissionRequiredMixin, View):
    permission_required = 'customers.add_customer'

    def post(self, request, *args, **kwargs):
        lead_id = request.session.get('lead_id_for_customer_create')
        if not lead_id:
            # если кто-то открыл /customers/new/ напрямую
            return redirect('leads:list')

        lead = get_object_or_404(Lead, pk=lead_id)

        # если уже есть customer — просто откроем его
        if hasattr(lead, 'customer'):
            return redirect('customers:detail', pk=lead.customer.pk)

        customer = Customer.objects.create(lead=lead)

        # очищаем session
        request.session.pop('lead_id_for_customer_create', None)

        # дальше по цепочке -> контракт
        return redirect('contracts:create_for_customer', customer_id=customer.pk)

    def get(self, request, *args, **kwargs):
        return redirect('leads:list')


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Lead
    template_name = 'customers/customers-edit.html'
    permission_required = 'customers.change_customer'

    # редактируем поля лида, которые логично менять у клиента
    fields = ['first_name', 'last_name', 'phone', 'email']

    def get_object(self, queryset=None):
        customer = get_object_or_404(Customer, pk=self.kwargs['pk'])
        return customer.lead

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # чтобы шаблон использовал object.pk (customer.pk), а не lead.pk
        ctx['object'] = get_object_or_404(Customer, pk=self.kwargs['pk'])
        return ctx

    def get_success_url(self):
        return reverse_lazy('customers:detail', kwargs={'pk': self.kwargs['pk']})
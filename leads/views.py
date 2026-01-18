from django.shortcuts import render

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Lead


class LeadListView(PermissionRequiredMixin, ListView):
    model = Lead
    template_name = 'leads/leads-list.html'
    permission_required = 'leads.view_lead'
    context_object_name = 'leads'


class LeadDetailView(PermissionRequiredMixin, DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'
    permission_required = 'leads.view_lead'


class LeadCreateView(PermissionRequiredMixin, CreateView):
    model = Lead
    fields = ['first_name', 'last_name', 'phone', 'email', 'ad']
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:list')
    permission_required = 'leads.add_lead'


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    model = Lead
    fields = ['first_name', 'last_name', 'phone', 'email', 'ad']
    template_name = 'leads/leads-edit.html'
    success_url = reverse_lazy('leads:list')
    permission_required = 'leads.change_lead'


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:list')
    permission_required = 'leads.delete_lead'

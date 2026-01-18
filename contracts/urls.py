from django.urls import path
from .views import *

app_name = 'contracts'

urlpatterns = [
    path('', ContractListView.as_view(), name='list'),
    path('new', ContractCreateView.as_view(), name='create'),
    path('new/', ContractCreateView.as_view(), name='create_slash'),
    path('for-customer/<int:customer_id>/new', ContractCreateForCustomerView.as_view(), name='create_for_customer'),
    path('<int:pk>', ContractDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', ContractUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', ContractDeleteView.as_view(), name='delete'),
]

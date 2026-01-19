from django.urls import path
from .views import (
    CustomerCreateFromLeadView,
    CustomerListView,
    CustomerDetailView,
    CustomerDeleteView,
    CustomerCreatePostView,
    CustomerUpdateView,
)

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='list'),
    path('from-lead/<int:lead_id>', CustomerCreateFromLeadView.as_view(), name='from_lead'),
    path('new/', CustomerCreatePostView.as_view(), name='new'),
    path('<int:pk>', CustomerDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', CustomerUpdateView.as_view(), name='edit'),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name='edit_slash'),
    path('<int:pk>/delete', CustomerDeleteView.as_view(), name='delete'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete_slash'),
]

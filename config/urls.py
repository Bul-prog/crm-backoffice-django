"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, logout_get
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', logout_get, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('products/', include('products.urls')),
    path('ads/', include('ads.urls')),
    path('leads/', include('leads.urls')),
    path('customers/', include('customers.urls')),
    path('contracts/', include('contracts.urls')),
]

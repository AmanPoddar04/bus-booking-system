"""
URL configuration for BusBookingSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

admin.site.site_title = "Bus Booking System (DEV)"
admin.site.site_header = "Bus Booking System Administration"
admin.site.index_title = "Admin Panel"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("booking.urls")),
    path("accounts/", include("allauth.urls")),
    path("logout", LogoutView.as_view()),
    path("booking/", include("booking.urls")),
]
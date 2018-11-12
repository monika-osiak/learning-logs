"""Definiuje wzorce adresów URL dla aplikacji users."""

from django.urls import re_path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # Strona logowania
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    # Strona wylogowania
    re_path(r'^logout/$', views.logout_view, name='logout'),
]

"""Rutas de la aplicación de cuentas."""

from django.urls import path

from .views import LoginView, MeView


urlpatterns = [
    path("auth/login", LoginView.as_view(), name="login"),
    path("me", MeView.as_view(), name="me"),
]


"""Rutas de la aplicación de cuentas."""

from django.urls import path

from .views import me, update_profile, check_email


urlpatterns = [
    # path("auth/google", GoogleAuthView.as_view(), name="google_auth"),  # DESHABILITADO
    path("me", me, name="me"),
    path("me/update", update_profile, name="update_profile"),
    path("check-email", check_email, name="check_email"),
]


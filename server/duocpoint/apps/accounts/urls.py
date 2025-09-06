"""Rutas de la aplicación de cuentas."""

from django.urls import path

from .views import me, update_profile, check_email, login, register


urlpatterns = [
    # path("auth/google", GoogleAuthView.as_view(), name="google_auth"),  # DESHABILITADO
    path("auth/login/", login, name="login"),
    path("auth/register/", register, name="register"),
    path("auth/me", me, name="me"),
    path("auth/me/update", update_profile, name="update_profile"),
    path("auth/check-email", check_email, name="check_email"),
]


"""Configuración del administrador para la app de cuentas."""

from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):  # pragma: no cover - interfaz de administración
    list_display = ("email", "name", "role")
    search_fields = ("email", "name")

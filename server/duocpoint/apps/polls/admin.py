"""Configuración de la interfaz de administración para encuestas."""

from django.contrib import admin

from .models import Poll, PollOpcion, PollVoto


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "multi", "cierra_at"]


@admin.register(PollOpcion)
class PollOpcionAdmin(admin.ModelAdmin):
    list_display = ["id", "poll", "texto"]


@admin.register(PollVoto)
class PollVotoAdmin(admin.ModelAdmin):
    list_display = ["id", "poll", "opcion", "usuario"]

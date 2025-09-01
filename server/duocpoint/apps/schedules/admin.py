"""Admin bindings for schedule models."""

from django.contrib import admin

from .models import Horario, ScheduleImport


@admin.register(ScheduleImport)
class ScheduleImportAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "status", "created_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "asignatura", "dia_semana", "inicio", "fin")
    readonly_fields = ("created_at", "updated_at")

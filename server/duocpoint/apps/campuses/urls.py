"""Rutas para la app de sedes."""

from django.urls import path

from .views import RecorridoPasoListView, SedeListView

urlpatterns = [
    path("sedes", SedeListView.as_view(), name="sede-list"),
    path("recorridos", RecorridoPasoListView.as_view(), name="recorrido-pasos"),
]

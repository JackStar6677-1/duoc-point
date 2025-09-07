from django.urls import path

from .views import (
    ScheduleImportCreateView,
    ScheduleImportDetailView,
    HorarioListCreateView,
    HorarioDetailView,
)

urlpatterns = [
    path("horarios/import/pdf", ScheduleImportCreateView.as_view()),
    path("horarios/import/<uuid:id>", ScheduleImportDetailView.as_view()),
    path("horarios", HorarioListCreateView.as_view()),
    path("horarios/<uuid:id>", HorarioDetailView.as_view()),
]

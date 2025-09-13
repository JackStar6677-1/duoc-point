from django.urls import path

from .views import (
    ScheduleImportCreateView,
    ScheduleImportDetailView,
    HorarioListCreateView,
    HorarioDetailView,
)

urlpatterns = [
    path("schedules/import/pdf", ScheduleImportCreateView.as_view()),
    path("schedules/import/<uuid:id>", ScheduleImportDetailView.as_view()),
    path("schedules/", HorarioListCreateView.as_view()),
    path("schedules/<uuid:id>", HorarioDetailView.as_view()),
]

"""Rutas públicas para la API de encuestas."""

from django.urls import path

from .views import PollCreateView, PollDetailView, PollVoteView

urlpatterns = [
    path("polls", PollCreateView.as_view(), name="poll-create"),
    path("polls/<int:pk>", PollDetailView.as_view(), name="poll-detail"),
    path("polls/<int:pk>/votar", PollVoteView.as_view(), name="poll-vote"),
]

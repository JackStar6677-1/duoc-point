"""Rutas de la aplicación de foros."""

from django.urls import path

from .views import (
    CommentCreateView,
    ForoListView,
    ModeracionListView,
    PostHideView,
    PostListCreateView,
    PostModeracionView,
    PostReporteView,
    PostReportesListView,
    PostVoteView,
)

urlpatterns = [
    path("foros", ForoListView.as_view(), name="foro-list"),
    path("posts", PostListCreateView.as_view(), name="post-list"),
    path("posts/<int:pk>/comentarios", CommentCreateView.as_view(), name="post-comments"),
    path("posts/<int:pk>/votar", PostVoteView.as_view(), name="post-vote"),
    path("posts/<int:pk>/reportar", PostReporteView.as_view(), name="post-report"),
    path("posts/<int:pk>/moderar", PostModeracionView.as_view(), name="post-moderate"),
    path("posts/<int:pk>/ocultar", PostHideView.as_view(), name="post-hide"),
    path("posts/<int:pk>/reportes", PostReportesListView.as_view(), name="post-reports"),
    path("moderacion", ModeracionListView.as_view(), name="moderation-list"),
]

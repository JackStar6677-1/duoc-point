"""Rutas de la aplicación de foros."""

from django.urls import path

from .views import (
    CommentCreateView,
    ForoListView,
    PostHideView,
    PostListCreateView,
    PostVoteView,
)

urlpatterns = [
    path("foros", ForoListView.as_view(), name="foro-list"),
    path("posts", PostListCreateView.as_view(), name="post-list"),
    path("posts/<int:pk>/comentarios", CommentCreateView.as_view(), name="post-comments"),
    path("posts/<int:pk>/votar", PostVoteView.as_view(), name="post-vote"),
    path("posts/<int:pk>/ocultar", PostHideView.as_view(), name="post-hide"),
]

"""Vistas simuladas del foro."""

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from duocpoint.apps.accounts.permissions import IsModerator


class PostViewSet(viewsets.ViewSet):
    """Acciones sobre posts del foro.

    La acción ``hide`` sirve como ejemplo donde sólo los usuarios con
    rol ``moderator`` pueden ejecutar dicha operación.
    """

    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"], permission_classes=[IsModerator])
    def hide(self, request, pk=None):  # pragma: no cover - acción de ejemplo
        return Response({"detail": f"post {pk} oculto"})


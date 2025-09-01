"""Vistas simuladas para la app de encuestas.

Sólo se implementa una vista mínima para ilustrar el uso de permisos.
En una implementación real se utilizaría un ``ModelViewSet`` completo.
"""

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from duocpoint.apps.accounts.permissions import IsModeratorOrDirector


class PollViewSet(viewsets.ViewSet):
    """Permite crear encuestas sólo a moderadores o directores."""

    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):  # pragma: no cover - vista de ejemplo
        return Response({"detail": "creado"})

    def get_permissions(self):  # pragma: no cover - vista de ejemplo
        if getattr(self, "action", None) == "create":
            perms = [IsModeratorOrDirector]
        else:
            perms = self.permission_classes
        return [p() for p in perms]


"""Generación de portafolio en PDF."""

from django.http import HttpResponse
from rest_framework import permissions, views
from drf_spectacular.utils import OpenApiTypes, extend_schema


class PortfolioPDFView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(responses={501: OpenApiTypes.STR})
    def get(self, request):
        """Informa que la generación de PDF no está disponible."""
        message = "La generación de PDF se encuentra deshabilitada en esta versión."
        return HttpResponse(message, content_type="text/plain", status=501)

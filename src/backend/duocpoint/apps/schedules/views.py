"""API views for schedule import and management."""

import os
from pathlib import Path

from django.conf import settings
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import ScheduleImport, Horario
from .serializers import ScheduleImportSerializer, HorarioSerializer
from .tasks import parse_schedule_pdf

import yaml

CONFIG_DIR = Path(settings.BASE_DIR).parent.parent / "config"
SECURITY_CONFIG_FILE = CONFIG_DIR / "security.yaml"

# Cargar configuración de seguridad con valores por defecto
try:
    SECURITY_CONF = yaml.safe_load(SECURITY_CONFIG_FILE.read_text())
except FileNotFoundError:
    # Configuración por defecto para desarrollo
    SECURITY_CONF = {
        "file_validation": {
            "max_file_size": 10485760,  # 10MB
            "allowed_extensions": [".pdf", ".jpg", ".jpeg", ".png", ".gif"]
        },
        "rate_limiting": {
            "requests_per_minute": 60,
            "requests_per_hour": 1000
        },
        "authentication": {
            "max_login_attempts": 5,
            "lockout_duration": 900
        }
    }


class ScheduleImportCreateView(generics.GenericAPIView):
    """Upload a PDF with the official schedule and queue a parsing task."""

    parser_classes = [MultiPartParser]
    serializer_class = ScheduleImportSerializer

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "authentication required"}, status=401)
        uploaded = request.FILES.get("file")
        if not uploaded:
            return Response({"detail": "file required"}, status=400)
        ext = os.path.splitext(uploaded.name)[1].lower()
        if ext not in SECURITY_CONF.get("allowed_import_exts", []):
            return Response({"detail": "invalid extension"}, status=400)
        max_mb = SECURITY_CONF.get("max_upload_mb", 10)
        if uploaded.size > max_mb * 1024 * 1024:
            return Response({"detail": "file too large"}, status=400)

        sched_import = ScheduleImport.objects.create(usuario=request.user, file=uploaded)
        parse_schedule_pdf.delay(str(sched_import.id))
        data = {"import_id": sched_import.id, "status": sched_import.status}
        return Response(data, status=status.HTTP_202_ACCEPTED)


class ScheduleImportDetailView(generics.RetrieveAPIView):
    queryset = ScheduleImport.objects.all()
    serializer_class = ScheduleImportSerializer
    lookup_field = "id"


class HorarioListCreateView(generics.ListCreateAPIView):
    serializer_class = HorarioSerializer

    def get_queryset(self):
        qs = Horario.objects.filter(usuario=self.request.user)
        dia = self.request.query_params.get("dia_semana")
        if dia is not None:
            qs = qs.filter(dia_semana=dia)
        return qs


class HorarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HorarioSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Horario.objects.filter(usuario=self.request.user)

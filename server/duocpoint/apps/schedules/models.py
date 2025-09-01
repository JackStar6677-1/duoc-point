"""Data models for user class schedules and their PDF imports."""

import uuid

from django.conf import settings
from django.db import models


class ScheduleImport(models.Model):
    """Stores uploaded PDF files for later parsing into :class:`Horario` blocks.

    The parsing task updates the ``status`` field and writes debug or warning
    messages to ``parse_log`` so administrators can diagnose problems.  The
    ``file`` field is limited to PDF uploads and validated in the API view.
    """

    STATUS_CHOICES = [
        ("queued", "queued"),
        ("processing", "processing"),
        ("done", "done"),
        ("failed", "failed"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="schedule_imports/")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="queued")
    parse_log = models.TextField(blank=True)
    timezone = models.CharField(max_length=64, default="America/Santiago")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"Import {self.id} ({self.status})"


class Horario(models.Model):
    """Represents a single class block for a user.

    ``fuente`` links to the :class:`ScheduleImport` that generated the block so
    the original data can be re‑parsed or inspected.  When a user manually edits
    a block the ``editable`` flag is kept ``True`` so later automatic updates can
    skip it.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dia_semana = models.IntegerField()
    inicio = models.TimeField()
    fin = models.TimeField()
    asignatura = models.CharField(max_length=255)
    sala = models.CharField(max_length=255, blank=True)
    fuente = models.ForeignKey(
        ScheduleImport, null=True, blank=True, on_delete=models.SET_NULL, related_name="horarios"
    )
    editable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.asignatura} ({self.dia_semana})"


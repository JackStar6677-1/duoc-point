"""Celery tasks for parsing schedule PDFs."""

import re
from pathlib import Path

from celery import shared_task
from django.conf import settings
from PyPDF2 import PdfReader
import pytz

from .models import ScheduleImport, Horario
from duocpoint.apps.notifications.tasks import schedule_class_alerts

DAY_MAP = {
    "Lunes": 0,
    "Martes": 1,
    "Miércoles": 2,
    "Jueves": 3,
    "Viernes": 4,
    "Sábado": 5,
    "Domingo": 6,
}

CONFIG_DIR = Path(settings.BASE_DIR).parent / "config"


@shared_task
def parse_schedule_pdf(import_id: str):
    """Parse the uploaded PDF and create :class:`Horario` entries.

    The parser expects embedded text where each line follows the pattern::

        Lunes 08:00-09:30 Algebra Sala B-101

    It normalises whitespace and extracts día, hora inicio/fin, asignatura y
    sala.  For PDFs escaneados sin texto se devuelve el estado ``failed``.  Si
    se habilita OCR en el futuro, este es el punto para llamar a una función
    ``parse_schedule_pdf_ocr`` que convierta las imágenes a texto antes de
    continuar.
    """

    imp = ScheduleImport.objects.get(id=import_id)
    imp.status = "processing"
    imp.save(update_fields=["status"])

    pytz.timezone(imp.timezone)  # ensures timezone string is valid

    try:
        reader = PdfReader(imp.file)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as exc:  # pragma: no cover - rare
        imp.status = "failed"
        imp.parse_log = str(exc)
        imp.save(update_fields=["status", "parse_log"])
        return

    if not text.strip():
        imp.status = "failed"
        imp.parse_log = "PDF escaneado sin texto detectable"
        imp.save(update_fields=["status", "parse_log"])
        return

    # Normalise spaces but keep line breaks for block detection
    text = re.sub(r"[ \t]+", " ", text)
    blocks = []
    for line in text.split("\n"):
        match = re.search(
            r"(Lunes|Martes|Miércoles|Jueves|Viernes|Sábado|Domingo) (\d{2}:\d{2})-(\d{2}:\d{2}) (.+?) (?:Sala|Lab|Aula)? ?([A-Za-z0-9-]+)?$",
            line.strip(),
        )
        if match:
            day, start, end, subject, sala = match.groups()
            blocks.append((DAY_MAP[day], start, end, subject.strip(), sala or ""))

    created = 0
    for dia, inicio, fin, asignatura, sala in blocks:
        Horario.objects.create(
            usuario=imp.usuario,
            dia_semana=dia,
            inicio=inicio,
            fin=fin,
            asignatura=asignatura,
            sala=sala,
            fuente=imp,
            editable=False,
        )
        created += 1

    imp.status = "done"
    imp.parse_log = f"{created} bloques creados"
    imp.save(update_fields=["status", "parse_log"])

    schedule_class_alerts.delay(str(imp.usuario_id))

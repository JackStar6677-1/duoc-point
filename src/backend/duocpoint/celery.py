"""Celery application for asynchronous tasks.

This module exposes the Celery app used by Django. It reads broker and
backend URLs from Django settings (``CELERY_*``). To start processing
queue jobs locally use::

    celery -A duocpoint worker -l info
    celery -A duocpoint beat -l info  # para tareas periódicas
"""

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "duocpoint.settings.dev")

app = Celery("duocpoint")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

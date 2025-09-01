"""Celery tasks for scheduling and sending push notifications."""

import json
from datetime import datetime, timedelta
from pathlib import Path

from celery import shared_task
from django.conf import settings
import pytz
from pywebpush import WebPushException, webpush
import yaml

from .models import PushSub
from duocpoint.apps.schedules.models import Horario

CONFIG_DIR = Path(settings.BASE_DIR).parent / "config"
PUSH_CONF = yaml.safe_load((CONFIG_DIR / "push.yaml").read_text())


@shared_task
def schedule_class_alerts(user_id: str):
    """Schedule push notifications 20 minutes before each class for 30 days."""

    tz = pytz.timezone("America/Santiago")
    today = datetime.now(tz).date()
    for horario in Horario.objects.filter(usuario_id=user_id):
        for i in range(30):
            day = today + timedelta(days=i)
            if day.weekday() != horario.dia_semana:
                continue
            start_dt = datetime.combine(day, horario.inicio, tz)
            alert_dt = start_dt - timedelta(minutes=20)
            send_class_push.apply_async(
                args=[user_id, str(horario.id), start_dt.isoformat(), alert_dt.isoformat()],
                eta=alert_dt,
            )


@shared_task
def send_class_push(user_id: str, horario_id, fecha_clase, hora_alerta, test_only=False):
    """Send a Web Push notification to all active subscriptions of a user."""

    subs = PushSub.objects.filter(usuario_id=user_id, activo=True)
    if not subs:
        return

    if test_only:
        title = "Prueba de notificación"
        body = "Service worker operativo"
    else:
        horario = Horario.objects.get(id=horario_id)
        title = "Tienes clase en 20 minutos"
        body = f"{horario.asignatura} - {horario.sala} ({horario.inicio})"

    payload = json.dumps({"title": title, "body": body})

    for sub in subs:
        try:
            webpush(
                {
                    "endpoint": sub.endpoint,
                    "keys": {"p256dh": sub.p256dh, "auth": sub.auth},
                },
                data=payload,
                vapid_private_key=PUSH_CONF["vapid_private"],
                vapid_public_key=PUSH_CONF["vapid_public"],
                vapid_claims={"sub": PUSH_CONF["subject"]},
            )
        except WebPushException:
            sub.activo = False
            sub.save(update_fields=["activo"])

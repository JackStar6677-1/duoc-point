"""Models for storing Web Push subscriptions."""

import uuid

from django.conf import settings
from django.db import models


class PushSub(models.Model):
    """Represents a Web Push subscription for a user."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    endpoint = models.TextField(unique=True)
    p256dh = models.TextField()
    auth = models.TextField()
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.endpoint


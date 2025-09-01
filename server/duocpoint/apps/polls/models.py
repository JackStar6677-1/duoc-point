"""Modelos de encuestas vinculadas a posts del foro.

Cada encuesta (:class:`Poll`) se asocia a un :class:`forum.models.Post` y
contiene varias opciones (:class:`PollOpcion`). Los votos se registran en
:class:`PollVoto` y por defecto se limita a un voto por usuario/opción. Este
módulo podría ampliarse para ofrecer resultados en tiempo real mediante
`Django Channels` u otras tecnologías de WebSockets.
"""

from django.conf import settings
from django.db import models


class Poll(models.Model):
    """Encuesta asociada a un :class:`forum.models.Post`."""

    post = models.OneToOneField(
        "forum.Post", on_delete=models.CASCADE, related_name="poll"
    )
    multi = models.BooleanField(default=False)
    cierra_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return f"Poll de {self.post_id}"


class PollOpcion(models.Model):
    """Opción posible dentro de una :class:`Poll`."""

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="opciones")
    texto = models.CharField(max_length=200)

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return self.texto


class PollVoto(models.Model):
    """Registro de votos por usuario y opción."""

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="votos")
    opcion = models.ForeignKey(
        PollOpcion, on_delete=models.CASCADE, related_name="votos"
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="poll_votes"
    )

    class Meta:
        unique_together = ("poll", "usuario", "opcion")

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return f"{self.usuario_id} -> {self.opcion_id}"

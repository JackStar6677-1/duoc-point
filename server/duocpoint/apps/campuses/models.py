"""Modelos de la aplicación de sedes.

Para efectos de este ejercicio sólo se define un modelo muy simple de
``Campus`` con un único campo ``name``. Este modelo sirve de referencia
para usuarios que deseen asociarse a una sede específica.
"""

from django.db import models


class Campus(models.Model):
    """Representa una sede del DUOC UC."""

    name = models.CharField(max_length=100)

    def __str__(self) -> str:  # pragma: no cover - representación sencilla
        return self.name


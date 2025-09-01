"""Modelos básicos para el foro de la aplicación."""

from django.conf import settings
from django.db import models


# Palabras que no se permiten en títulos o cuerpos de posts. Si una
# aparece, el post queda en estado de "revisión". Ajusta esta lista para
# modificar las reglas de moderación.
BANNED_WORDS = {"malo", "ofensivo"}


class Foro(models.Model):
    """Espacio de discusión filtrado por sede y carrera."""

    sede = models.ForeignKey("campuses.Sede", on_delete=models.CASCADE, related_name="foros")
    carrera = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return self.titulo


class Post(models.Model):
    """Publicación realizada dentro de un :class:`Foro`."""

    class Estado(models.TextChoices):
        PUBLICADO = "publicado", "Publicado"
        REVISION = "revision", "En revisión"
        OCULTO = "oculto", "Oculto"

    foro = models.ForeignKey(Foro, on_delete=models.CASCADE, related_name="posts")
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    anonimo = models.BooleanField(default=False)
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    score = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PUBLICADO)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return self.titulo


class Comentario(models.Model):
    """Comentario asociado a un :class:`Post`."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comentarios"
    )
    anonimo = models.BooleanField(default=False)
    cuerpo = models.TextField()
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return f"Comentario de {self.usuario_id}"


class VotoPost(models.Model):
    """Registro de votos de usuarios sobre un post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="votos")
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post_votes"
    )
    valor = models.IntegerField(choices=[(-1, -1), (0, 0), (1, 1)])

    class Meta:
        unique_together = ("post", "usuario")


class VotoComentario(models.Model):
    """Registro de votos sobre un comentario."""

    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name="votos")
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_votes"
    )
    valor = models.IntegerField(choices=[(-1, -1), (0, 0), (1, 1)])

    class Meta:
        unique_together = ("comentario", "usuario")


class ModeracionEvent(models.Model):
    """Historial mínimo de acciones de moderación."""

    objeto_tipo = models.CharField(max_length=20)
    objeto_id = models.PositiveIntegerField()
    score = models.IntegerField(default=0)
    accion = models.CharField(max_length=50)
    razones_json = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return f"{self.accion} {self.objeto_tipo}:{self.objeto_id}"


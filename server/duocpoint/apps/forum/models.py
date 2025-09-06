"""Modelos básicos para el foro de la aplicación."""

from django.conf import settings
from django.db import models


# Palabras que no se permiten en títulos o cuerpos de posts. Si una
# aparece, el post queda en estado de "revisión". Ajusta esta lista para
# modificar las reglas de moderación.
BANNED_WORDS = {
    "malo", "ofensivo", "odio", "violencia", "drogas", "alcohol", 
    "sexo", "pornografia", "spam", "estafa", "fraude", "hack",
    "virus", "malware", "phishing", "scam", "fake", "mentira"
}

# Palabras que requieren moderación manual
MODERATION_WORDS = {
    "política", "religión", "discriminación", "racismo", "sexismo",
    "homofobia", "transfobia", "bullying", "acoso", "amenaza"
}


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
        RECHAZADO = "rechazado", "Rechazado"

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
    updated_at = models.DateTimeField(auto_now=True)
    
    # Campos de moderación
    moderado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="posts_moderados"
    )
    razon_moderacion = models.TextField(blank=True)
    moderado_at = models.DateTimeField(null=True, blank=True)
    
    # Campos de reportes
    total_reportes = models.PositiveIntegerField(default=0)
    ultimo_reporte_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:  # pragma: no cover - representación simple
        return self.titulo
    
    def verificar_contenido(self):
        """Verifica el contenido del post y determina el estado apropiado."""
        texto = f"{self.titulo} {self.cuerpo}".lower()
        
        # Verificar palabras prohibidas
        if any(bad in texto for bad in BANNED_WORDS):
            return Post.Estado.REVISION
        
        # Verificar palabras que requieren moderación
        if any(mod in texto for mod in MODERATION_WORDS):
            return Post.Estado.REVISION
            
        return Post.Estado.PUBLICADO
    
    def moderar(self, moderador, accion, razon=""):
        """Aplica una acción de moderación al post."""
        from django.utils import timezone
        
        self.moderado_por = moderador
        self.razon_moderacion = razon
        self.moderado_at = timezone.now()
        
        if accion == "aprobar":
            self.estado = Post.Estado.PUBLICADO
        elif accion == "rechazar":
            self.estado = Post.Estado.RECHAZADO
        elif accion == "ocultar":
            self.estado = Post.Estado.OCULTO
            
        self.save()
        
        # Registrar evento de moderación
        ModeracionEvent.objects.create(
            objeto_tipo="post",
            objeto_id=self.id,
            accion=accion,
            razones_json={"razon": razon, "moderador": moderador.id}
        )
    
    def reportar(self, usuario, tipo, descripcion=""):
        """Registra un reporte sobre el post."""
        from django.utils import timezone
        
        reporte, created = PostReporte.objects.get_or_create(
            post=self,
            usuario=usuario,
            defaults={
                "tipo": tipo,
                "descripcion": descripcion
            }
        )
        
        if created:
            self.total_reportes += 1
            self.ultimo_reporte_at = timezone.now()
            self.save(update_fields=["total_reportes", "ultimo_reporte_at"])
            
            # Si hay muchos reportes, enviar a revisión
            if self.total_reportes >= 3:
                self.estado = Post.Estado.REVISION
                self.save(update_fields=["estado"])
        
        return reporte


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


class PostReporte(models.Model):
    """Reportes de usuarios sobre posts inapropiados."""
    
    class TipoReporte(models.TextChoices):
        SPAM = "spam", "Spam"
        CONTENIDO_INAPROPIADO = "contenido_inapropiado", "Contenido Inapropiado"
        ACOSO = "acoso", "Acoso"
        DESINFORMACION = "desinformacion", "Desinformación"
        VIOLENCIA = "violencia", "Violencia"
        OTRO = "otro", "Otro"
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reportes")
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="reportes_realizados"
    )
    tipo = models.CharField(max_length=30, choices=TipoReporte.choices)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("post", "usuario")
    
    def __str__(self) -> str:
        return f"Reporte de {self.usuario.name} sobre {self.post.titulo}"


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


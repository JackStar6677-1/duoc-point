"""Serializadores para la app de foros."""

from rest_framework import serializers

from .models import Comentario, Foro, Post, PostReporte


class ForoSerializer(serializers.ModelSerializer):
    """Representa un foro temático."""

    class Meta:
        model = Foro
        fields = ["id", "sede", "carrera", "titulo", "slug"]


class PostSerializer(serializers.ModelSerializer):
    """Serializa posts para listado y creación."""
    
    usuario_name = serializers.CharField(source="usuario.name", read_only=True)
    total_comentarios = serializers.SerializerMethodField()
    total_reportes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "foro",
            "usuario",
            "usuario_name",
            "anonimo",
            "titulo",
            "cuerpo",
            "score",
            "estado",
            "created_at",
            "updated_at",
            "total_comentarios",
            "total_reportes",
            "moderado_por",
            "razon_moderacion",
            "moderado_at",
        ]
        read_only_fields = [
            "usuario", "score", "estado", "created_at", "updated_at",
            "total_comentarios", "total_reportes", "moderado_por", 
            "razon_moderacion", "moderado_at"
        ]
    
    def get_total_comentarios(self, obj):
        return obj.comentarios.count()


class ComentarioSerializer(serializers.ModelSerializer):
    """Serializador de comentarios."""

    class Meta:
        model = Comentario
        fields = ["id", "post", "usuario", "anonimo", "cuerpo", "score", "created_at"]
        read_only_fields = ["post", "usuario", "score", "created_at"]


class VoteSerializer(serializers.Serializer):
    """Payload esperado para registrar un voto."""

    valor = serializers.IntegerField()


class ScoreSerializer(serializers.Serializer):
    """Respuesta que devuelve el score actualizado."""

    score = serializers.IntegerField()


class PostReporteSerializer(serializers.ModelSerializer):
    """Serializer para reportes de posts."""
    
    usuario_name = serializers.CharField(source="usuario.name", read_only=True)
    
    class Meta:
        model = PostReporte
        fields = [
            "id", "post", "usuario", "usuario_name", "tipo", 
            "descripcion", "created_at"
        ]
        read_only_fields = ["usuario", "created_at"]


class ModeracionSerializer(serializers.Serializer):
    """Serializer para acciones de moderación."""
    
    accion = serializers.ChoiceField(choices=["aprobar", "rechazar", "ocultar"])
    razon = serializers.CharField(required=False, allow_blank=True)


class ForumDetailSerializer(serializers.Serializer):
    """Mensaje simple para respuestas sin contenido estructurado."""

    detail = serializers.CharField()

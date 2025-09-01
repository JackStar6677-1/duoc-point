"""Serializadores para la app de foros."""

from rest_framework import serializers

from .models import Comentario, Foro, Post


class ForoSerializer(serializers.ModelSerializer):
    """Representa un foro temático."""

    class Meta:
        model = Foro
        fields = ["id", "sede", "carrera", "titulo", "slug"]


class PostSerializer(serializers.ModelSerializer):
    """Serializa posts para listado y creación."""

    class Meta:
        model = Post
        fields = [
            "id",
            "foro",
            "usuario",
            "anonimo",
            "titulo",
            "cuerpo",
            "score",
            "estado",
            "created_at",
        ]
        read_only_fields = ["usuario", "score", "estado", "created_at"]


class ComentarioSerializer(serializers.ModelSerializer):
    """Serializador de comentarios."""

    class Meta:
        model = Comentario
        fields = ["id", "post", "usuario", "anonimo", "cuerpo", "score", "created_at"]
        read_only_fields = ["post", "usuario", "score", "created_at"]

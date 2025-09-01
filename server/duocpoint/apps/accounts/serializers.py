"""Serializadores utilizados en la app de cuentas."""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Representación básica del usuario para respuestas API."""

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "name", "campus", "career", "role"]


class LoginSerializer(serializers.Serializer):
    """Datos requeridos para autenticarse."""

    email = serializers.EmailField()
    password = serializers.CharField()


class TokenPairSerializer(serializers.Serializer):
    """Tokens JWT de acceso y refresco."""

    access = serializers.CharField()
    refresh = serializers.CharField()


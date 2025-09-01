"""Serializadores utilizados en la app de cuentas."""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Representación básica del usuario para respuestas API."""

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "name", "campus", "career", "role"]


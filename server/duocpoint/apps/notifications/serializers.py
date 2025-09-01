"""Serializers for push notification subscriptions."""

from rest_framework import serializers
from .models import PushSub


class PushSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushSub
        fields = ["endpoint", "p256dh", "auth"]

    def create(self, validated_data):
        user = self.context["request"].user
        sub, _ = PushSub.objects.update_or_create(
            usuario=user,
            endpoint=validated_data["endpoint"],
            defaults={
                "p256dh": validated_data["p256dh"],
                "auth": validated_data["auth"],
                "activo": True,
            },
        )
        return sub

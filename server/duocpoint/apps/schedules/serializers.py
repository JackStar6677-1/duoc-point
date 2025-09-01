"""Serializers for schedule import and blocks."""

from rest_framework import serializers
from .models import ScheduleImport, Horario


class ScheduleImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleImport
        fields = ["id", "status", "parse_log"]
        read_only_fields = ["id", "status", "parse_log"]


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = [
            "id",
            "dia_semana",
            "inicio",
            "fin",
            "asignatura",
            "sala",
            "editable",
        ]
        read_only_fields = ["id", "editable"]

    def create(self, validated_data):
        validated_data["usuario"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.editable = True
        return super().update(instance, validated_data)

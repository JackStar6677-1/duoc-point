"""Serializadores para crear y visualizar encuestas."""

from rest_framework import serializers

from .models import Poll, PollOpcion, PollVoto


class PollOptionSerializer(serializers.ModelSerializer):
    """Representa una opción y su conteo de votos."""

    votos = serializers.IntegerField(read_only=True)

    class Meta:
        model = PollOpcion
        fields = ["id", "texto", "votos"]


class PollSerializer(serializers.ModelSerializer):
    """Detalle de la encuesta incluyendo resultados."""

    opciones = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ["id", "post", "multi", "cierra_at", "opciones"]

    def get_opciones(self, obj):
        return [
            {"id": o.id, "texto": o.texto, "votos": o.votos.count()}
            for o in obj.opciones.all()
        ]


class PollCreateSerializer(serializers.ModelSerializer):
    """Crea una encuesta con un listado de opciones."""

    opciones = serializers.ListField(
        child=serializers.CharField(), write_only=True, min_length=1
    )

    class Meta:
        model = Poll
        fields = ["id", "post", "multi", "cierra_at", "opciones"]

    def create(self, validated_data):
        opciones = validated_data.pop("opciones")
        poll = Poll.objects.create(**validated_data)
        for texto in opciones:
            PollOpcion.objects.create(poll=poll, texto=texto)
        return poll


class PollVoteSerializer(serializers.Serializer):
    """Valida y registra votos para una encuesta."""

    opciones = serializers.ListField(
        child=serializers.IntegerField(), allow_empty=False
    )

    def validate(self, attrs):
        poll: Poll = self.context["poll"]
        opcion_ids = attrs["opciones"]
        opciones = PollOpcion.objects.filter(poll=poll, id__in=opcion_ids)
        if opciones.count() != len(opcion_ids):
            raise serializers.ValidationError("opción inválida")
        user = self.context["request"].user
        # verificar votos existentes
        if PollVoto.objects.filter(poll=poll, usuario=user, opcion__in=opciones).exists():
            raise serializers.ValidationError("ya votaste esta opción")
        if not poll.multi and PollVoto.objects.filter(poll=poll, usuario=user).exists():
            raise serializers.ValidationError("esta encuesta permite un solo voto")
        attrs["_opciones_objs"] = list(opciones)
        return attrs

    def create(self, validated_data):
        poll: Poll = self.context["poll"]
        user = self.context["request"].user
        for opcion in validated_data["_opciones_objs"]:
            PollVoto.objects.create(poll=poll, opcion=opcion, usuario=user)
        return poll

"""Vistas para crear encuestas y registrar votos.

Estas vistas ilustran un flujo básico de encuestas. Se podrían extender
para ofrecer resultados en tiempo real utilizando Django Channels u
otros mecanismos de notificaciones.
"""

from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from duocpoint.apps.accounts.permissions import IsModeratorOrDirector

from .models import Poll
from .serializers import PollCreateSerializer, PollSerializer, PollVoteSerializer


class PollCreateView(generics.CreateAPIView):
    """Crea una nueva encuesta asociada a un post del foro."""

    serializer_class = PollCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsModeratorOrDirector]

    def create(self, request, *args, **kwargs):
        """Retorna la encuesta con sus opciones al crearla."""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        poll = serializer.save()
        return Response(
            PollSerializer(poll).data, status=status.HTTP_201_CREATED
        )


class PollDetailView(generics.RetrieveAPIView):
    """Devuelve los detalles de una encuesta con sus resultados."""

    queryset = Poll.objects.all().prefetch_related("opciones__votos")
    serializer_class = PollSerializer


class PollVoteView(APIView):
    """Registra votos del usuario autenticado para una encuesta."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollVoteSerializer(
            data=request.data, context={"poll": poll, "request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "ok"})

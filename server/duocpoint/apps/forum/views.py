"""Vistas para la API del foro."""

from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from duocpoint.apps.accounts.permissions import IsModerator

from .models import BANNED_WORDS, Comentario, Foro, Post, VotoPost
from .serializers import (
    ComentarioSerializer,
    ForumDetailSerializer,
    ForoSerializer,
    PostSerializer,
    ScoreSerializer,
    VoteSerializer,
)


class ForoListView(generics.ListAPIView):
    """Lista los foros disponibles filtrando por sede y carrera.

    El frontend utilizará este endpoint para mostrar los foros
    pertinentes al usuario según su sede y carrera.
    """

    serializer_class = ForoSerializer

    def get_queryset(self):
        queryset = Foro.objects.all()
        sede = self.request.query_params.get("sede")
        carrera = self.request.query_params.get("carrera")
        if sede:
            queryset = queryset.filter(sede__slug=sede)
        if carrera:
            queryset = queryset.filter(carrera=carrera)
        return queryset


class PostListCreateView(generics.ListCreateAPIView):
    """Lista posts de un foro y permite crear nuevas publicaciones."""

    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        foro_id = self.request.query_params.get("foro_id")
        if foro_id:
            queryset = queryset.filter(foro_id=foro_id)
        orden = self.request.query_params.get("orden", "nuevo")
        if orden == "top":
            queryset = queryset.order_by("-score")
        else:
            queryset = queryset.order_by("-created_at")
        return queryset

    def perform_create(self, serializer):
        texto = (
            f"{serializer.validated_data['titulo']} {serializer.validated_data['cuerpo']}".lower()
        )
        estado = Post.Estado.PUBLICADO
        if any(bad in texto for bad in BANNED_WORDS):
            estado = Post.Estado.REVISION
        serializer.save(usuario=self.request.user, estado=estado)


class CommentCreateView(generics.CreateAPIView):
    """Crea un comentario dentro de un post."""

    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        serializer.save(post=post, usuario=self.request.user)


class PostVoteView(APIView):
    """Registra el voto del usuario para un post."""
    @extend_schema(request=VoteSerializer, responses=ScoreSerializer)
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        try:
            valor = int(request.data.get("valor"))
        except (TypeError, ValueError):
            return Response({"detail": "valor inválido"}, status=status.HTTP_400_BAD_REQUEST)
        if valor not in (-1, 0, 1):
            return Response({"detail": "valor inválido"}, status=status.HTTP_400_BAD_REQUEST)
        VotoPost.objects.update_or_create(
            post=post, usuario=request.user, defaults={"valor": valor}
        )
        post.score = post.votos.aggregate(score=Sum("valor"))["score"] or 0
        post.save(update_fields=["score"])
        return Response({"score": post.score})


class PostHideView(generics.GenericAPIView):
    """Permite a moderadores ocultar posts."""

    permission_classes = [IsModerator]
    serializer_class = ForumDetailSerializer

    @extend_schema(responses=ForumDetailSerializer)
    def post(self, request, pk):  # pragma: no cover - acción administrativa
        post = get_object_or_404(Post, pk=pk)
        post.estado = Post.Estado.OCULTO
        post.save(update_fields=["estado"])
        return Response({"detail": "post oculto"})

"""Vistas de la aplicación de cuentas."""

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer


class LoginView(APIView):
    """Realiza un login básico basado en correo y contraseña.

    Actualmente sólo valida que el correo pertenezca al dominio
    institucional. No existe lógica de recuperación de contraseña ni
    flujo de activación.  En el futuro esta vista debería reemplazarse
    por un proceso completo de autenticación.
    """

    authentication_classes: list = []
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({"detail": "email y password son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)
        if user is None:
            # authenticate ya valida el dominio vía el modelo
            return Response({"detail": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})


class MeView(APIView):
    """Retorna los datos del usuario autenticado."""

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


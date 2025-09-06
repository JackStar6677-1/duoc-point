"""Views para autenticación y gestión de usuarios."""

import json
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema

User = get_user_model()


@extend_schema(
    summary="Obtener información del usuario actual",
    responses={200: {"description": "Información del usuario"}}
)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def me(request):
    """Obtiene información del usuario actual."""
    user = request.user
    
    return Response({
        'id': user.id,
        'email': user.email,
        'name': user.name,
        'campus': user.campus.nombre if user.campus else None,
        'career': user.career,
        'role': user.role,
        'es_duoc': user.es_duoc,
        'es_gmail': user.es_gmail,
        'es_estudiante_gmail': user.es_estudiante_gmail,
        'telefono': user.telefono,
        'linkedin_url': user.linkedin_url,
        'github_url': user.github_url,
        'date_joined': user.date_joined
    })


@extend_schema(
    summary="Actualizar perfil del usuario",
    responses={200: {"description": "Perfil actualizado exitosamente"}}
)
@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated])
def update_profile(request):
    """Actualiza el perfil del usuario."""
    user = request.user
    
    # Campos permitidos para actualizar
    allowed_fields = ['name', 'career', 'telefono', 'linkedin_url', 'github_url']
    
    for field in allowed_fields:
        if field in request.data:
            setattr(user, field, request.data[field])
    
    try:
        user.save()
        return Response({'message': 'Perfil actualizado exitosamente'})
    except Exception as e:
        return Response(
            {'error': f'Error actualizando perfil: {str(e)}'}, 
            status=status.HTTP_400_BAD_REQUEST
        )


@extend_schema(
    summary="Verificar si un email está permitido",
    responses={200: {"description": "Estado del email"}}
)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def check_email(request):
    """Verifica si un email está permitido en el sistema."""
    email = request.data.get('email', '').lower()
    
    if email.endswith('@duocuc.cl'):
        return Response({
            'allowed': True,
            'type': 'duoc',
            'message': 'Email institucional válido'
        })
    elif email.endswith('@gmail.com'):
        return Response({
            'allowed': True,
            'type': 'gmail',
            'message': 'Email Gmail válido para estudiantes'
        })
    else:
        return Response({
            'allowed': False,
            'type': 'not_allowed',
            'message': 'Solo se permiten correos @duocuc.cl o @gmail.com'
        })
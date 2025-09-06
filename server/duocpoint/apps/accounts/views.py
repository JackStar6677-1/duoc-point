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
from google.oauth2 import id_token
from google.auth.transport import requests

User = get_user_model()


class GoogleAuthView(APIView):
    """View para autenticación con Google OAuth."""
    
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(
        summary="Autenticación con Google",
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'credential': {'type': 'string', 'description': 'Token de Google OAuth'}
                },
                'required': ['credential']
            }
        },
        responses={
            200: {
                'description': 'Autenticación exitosa',
                'type': 'object',
                'properties': {
                    'access': {'type': 'string'},
                    'refresh': {'type': 'string'},
                    'user': {'type': 'object'}
                }
            },
            400: {'description': 'Token inválido'},
            403: {'description': 'Email no permitido'}
        }
    )
    def post(self, request):
        """Autentica un usuario con Google OAuth."""
        try:
            credential = request.data.get('credential')
            if not credential:
                return Response(
                    {'error': 'Token de Google requerido'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Verificar token con Google
            idinfo = id_token.verify_oauth2_token(
                credential, 
                requests.Request(), 
                settings.GOOGLE_OAUTH_CLIENT_ID
            )
            
            email = idinfo.get('email')
            name = idinfo.get('name', '')
            picture = idinfo.get('picture', '')
            
            if not email:
                return Response(
                    {'error': 'Email no encontrado en el token'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Verificar que el email sea permitido
            if not (email.lower().endswith('@duocuc.cl') or email.lower().endswith('@gmail.com')):
                return Response(
                    {'error': 'Solo se permiten correos @duocuc.cl o @gmail.com'}, 
                    status=status.HTTP_403_FORBIDDEN
                )
            
            # Buscar o crear usuario
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    'name': name,
                    'es_estudiante_gmail': email.lower().endswith('@gmail.com')
                }
            )
            
            if created:
                # Usuario nuevo - configurar campos básicos
                user.name = name
                user.es_estudiante_gmail = email.lower().endswith('@gmail.com')
                user.save()
            
            # Generar tokens JWT
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            
            # Información del usuario para el frontend
            user_data = {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'campus': user.campus.nombre if user.campus else None,
                'career': user.career,
                'role': user.role,
                'es_duoc': user.es_duoc,
                'es_gmail': user.es_gmail,
                'es_estudiante_gmail': user.es_estudiante_gmail,
                'picture': picture if user.es_gmail else None
            }
            
            return Response({
                'access': str(access_token),
                'refresh': str(refresh),
                'user': user_data,
                'created': created
            })
            
        except ValueError as e:
            return Response(
                {'error': f'Token inválido: {str(e)}'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': f'Error en autenticación: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@extend_schema(
    summary="Obtener información del usuario actual",
    responses={
        200: {
            'description': 'Información del usuario',
            'type': 'object',
            'properties': {
                'id': {'type': 'integer'},
                'email': {'type': 'string'},
                'name': {'type': 'string'},
                'campus': {'type': 'string'},
                'career': {'type': 'string'},
                'role': {'type': 'string'},
                'es_duoc': {'type': 'boolean'},
                'es_gmail': {'type': 'boolean'},
                'es_estudiante_gmail': {'type': 'boolean'}
            }
        }
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
    request={
        'application/json': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'career': {'type': 'string'},
                'telefono': {'type': 'string'},
                'linkedin_url': {'type': 'string'},
                'github_url': {'type': 'string'}
            }
        }
    },
    responses={
        200: {'description': 'Perfil actualizado exitosamente'},
        400: {'description': 'Datos inválidos'}
    }
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
    responses={
        200: {
            'description': 'Estado del email',
            'type': 'object',
            'properties': {
                'allowed': {'type': 'boolean'},
                'type': {'type': 'string', 'enum': ['duoc', 'gmail', 'not_allowed']}
            }
        }
    }
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
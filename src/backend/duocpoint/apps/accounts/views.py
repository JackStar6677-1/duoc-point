"""Views para autenticación y gestión de usuarios."""

import json
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from .models import User

User = get_user_model()


@extend_schema(
    summary="Obtener información del usuario actual",
    responses={200: {"description": "Información del usuario"}}
)
@csrf_exempt
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


@extend_schema(
    summary="Iniciar sesión",
    responses={200: {"description": "Login exitoso"}, 400: {"description": "Credenciales inválidas"}}
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    """Inicia sesión con email y contraseña."""
    try:
        # Obtener datos del request
        if hasattr(request, 'data'):
            email = request.data.get('email', '').lower()
            password = request.data.get('password', '')
        else:
            # Fallback para request.POST
            email = request.POST.get('email', '').lower()
            password = request.POST.get('password', '')
        
        if not email or not password:
            return Response(
                {'detail': 'Email y contraseña son requeridos'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Buscar usuario por email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'detail': 'Credenciales inválidas'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Verificar contraseña
        if user.check_password(password):
            # Generar tokens JWT
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'name': user.name,
                    'role': user.role,
                    'campus': user.campus.nombre if user.campus else None,
                    'career': user.career
                }
            })
        else:
            return Response(
                {'detail': 'Credenciales inválidas'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
            
    except Exception as e:
        return Response(
            {'detail': f'Error en el servidor: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@extend_schema(
    summary="Registrar nuevo usuario",
    responses={201: {"description": "Usuario creado exitosamente"}, 400: {"description": "Datos inválidos"}}
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    """Registra un nuevo usuario."""
    email = request.data.get('email', '').lower()
    password = request.data.get('password', '')
    name = request.data.get('name', '')
    role = request.data.get('role', 'student')
    career = request.data.get('career', '')
    campus_id = request.data.get('campus', 1)
    
    # Validaciones
    if not all([email, password, name, career]):
        return Response(
            {'detail': 'Todos los campos son requeridos'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if len(password) < 8:
        return Response(
            {'detail': 'La contraseña debe tener al menos 8 caracteres'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Verificar si el email ya existe
    if User.objects.filter(email=email).exists():
        return Response(
            {'detail': 'Este email ya está registrado'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Crear usuario
        user = User.objects.create_user(
            email=email,
            password=password,
            name=name,
            role=role,
            career=career,
            campus_id=campus_id
        )
        
        # Generar tokens JWT
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'role': user.role,
                'campus': user.campus.nombre if user.campus else None,
                'career': user.career
            }
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response(
            {'detail': f'Error creando usuario: {str(e)}'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
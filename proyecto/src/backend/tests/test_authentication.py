"""
Tests para el sistema de autenticación de DuocPoint
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from unittest.mock import patch
from duocpoint.apps.campuses.models import Sede

User = get_user_model()


class AuthenticationTestCase(APITestCase):
    """Tests para el sistema de autenticación"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        # Crear una sede de prueba
        self.sede = Sede.objects.create(
            slug='test-campus',
            nombre='Campus de Prueba',
            direccion='Dirección de Prueba',
            lat=-33.4489,
            lng=-70.6693
        )
        
        self.user_data = {
            'email': 'test@duocuc.cl',
            'password': 'testpass123',
            'name': 'Test User',
            'role': 'student',
            'campus': self.sede.id,
            'career': 'Ingeniería en Informática'
        }
    
    def test_user_registration_duocuc_email(self):
        """Test: Usuario puede registrarse con email @duocuc.cl"""
        response = self.client.post('/api/auth/register/', self.user_data)
        if response.status_code != status.HTTP_201_CREATED:
            print(f"Error response: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='test@duocuc.cl').exists())
    
    def test_user_registration_gmail_email(self):
        """Test: Usuario puede registrarse con email @gmail.com"""
        self.user_data['email'] = 'test@gmail.com'
        response = self.client.post('/api/auth/register/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='test@gmail.com').exists())
    
    def test_user_registration_invalid_email(self):
        """Test: Usuario no puede registrarse con email inválido"""
        self.user_data['email'] = 'test@hotmail.com'
        response = self.client.post('/api/auth/register/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(email='test@hotmail.com').exists())
    
    def test_user_login_success(self):
        """Test: Usuario puede iniciar sesión exitosamente"""
        user_data_copy = self.user_data.copy()
        user_data_copy['campus'] = self.sede  # Para create_user necesitamos la instancia
        user = User.objects.create_user(**user_data_copy)
        login_data = {
            'email': 'test@duocuc.cl',
            'password': 'testpass123'
        }
        response = self.client.post('/api/auth/login/', login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
    
    def test_user_login_invalid_credentials(self):
        """Test: Usuario no puede iniciar sesión con credenciales inválidas"""
        login_data = {
            'email': 'test@duocuc.cl',
            'password': 'wrongpassword'
        }
        response = self.client.post('/api/auth/login/', login_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_jwt_token_refresh(self):
        """Test: Usuario puede refrescar token JWT"""
        user_data_copy = self.user_data.copy()
        user_data_copy['campus'] = self.sede  # Para create_user necesitamos la instancia
        user = User.objects.create_user(**user_data_copy)
        refresh = RefreshToken.for_user(user)
        refresh_data = {'refresh': str(refresh)}
        response = self.client.post('/api/auth/refresh/', refresh_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
    
    def test_protected_endpoint_access(self):
        """Test: Endpoint protegido requiere autenticación"""
        response = self.client.get('/api/auth/me')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_authenticated_endpoint_access(self):
        """Test: Usuario autenticado puede acceder a endpoint protegido"""
        user_data_copy = self.user_data.copy()
        user_data_copy['campus'] = self.sede  # Para create_user necesitamos la instancia
        user = User.objects.create_user(**user_data_copy)
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/auth/me')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@duocuc.cl')


class UserModelTestCase(TestCase):
    """Tests para el modelo de Usuario"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        # Crear una sede de prueba
        self.sede = Sede.objects.create(
            slug='test-campus',
            nombre='Campus de Prueba',
            direccion='Dirección de Prueba',
            lat=-33.4489,
            lng=-70.6693
        )
    
    def test_user_creation(self):
        """Test: Usuario puede ser creado correctamente"""
        user = User.objects.create_user(
            email='test@duocuc.cl',
            password='testpass123',
            name='Test User',
            role='student',
            campus=self.sede,
            career='Ingeniería en Informática'
        )
        self.assertEqual(user.email, 'test@duocuc.cl')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.role, 'student')
        self.assertTrue(user.check_password('testpass123'))
    
    def test_user_str_representation(self):
        """Test: Representación string del usuario"""
        user = User.objects.create_user(
            email='test@duocuc.cl',
            password='testpass123',
            name='Test User'
        )
        self.assertEqual(str(user), 'test@duocuc.cl')
    
    def test_user_email_validation(self):
        """Test: Validación de email del usuario"""
        # Email válido @duocuc.cl
        user = User.objects.create_user(
            email='test@duocuc.cl',
            password='testpass123'
        )
        self.assertTrue(user.es_duoc)
        
        # Email válido @gmail.com
        user = User.objects.create_user(
            email='test@gmail.com',
            password='testpass123'
        )
        self.assertTrue(user.es_estudiante_gmail)
        
        # Email inválido
        from django.core.exceptions import ValidationError
        with self.assertRaises(ValidationError):
            User.objects.create_user(
                email='test@hotmail.com',
                password='testpass123'
            )

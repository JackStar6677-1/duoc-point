#!/usr/bin/env python3
"""
Script para probar el login de usuarios
"""

import os
import sys
import django
import requests

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duocpoint.settings.dev')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def test_login():
    """Probar el login de usuarios de prueba."""
    
    print("🧪 Probando login de usuarios...")
    
    # Usuarios de prueba
    test_users = [
        {
            'email': 'admin@duocuc.cl',
            'password': 'admin123',
            'role': 'admin'
        },
        {
            'email': 'estudiante@gmail.com',
            'password': 'estudiante123',
            'role': 'student'
        },
        {
            'email': 'profesor@duocuc.cl',
            'password': 'profesor123',
            'role': 'teacher'
        },
        {
            'email': 'moderador@duocuc.cl',
            'password': 'moderador123',
            'role': 'moderator'
        }
    ]
    
    # Verificar que los usuarios existen
    print("\n📋 Verificando usuarios en la base de datos:")
    for user_data in test_users:
        email = user_data['email']
        try:
            user = User.objects.get(email=email)
            print(f"✅ {email} - {user.name} ({user.role})")
        except User.DoesNotExist:
            print(f"❌ {email} - NO ENCONTRADO")
    
    print(f"\n🔑 Credenciales para probar en el navegador:")
    print(f"   📍 URL: http://localhost:8000/login.html")
    print(f"   👤 Usuarios disponibles:")
    for user_data in test_users:
        print(f"      - {user_data['email']} / {user_data['password']} ({user_data['role']})")
    
    print(f"\n💡 Instrucciones:")
    print(f"   1. Abre http://localhost:8000/login.html en tu navegador")
    print(f"   2. Haz clic en cualquiera de los botones de usuarios de prueba")
    print(f"   3. Haz clic en 'Iniciar Sesión'")
    print(f"   4. Deberías ser redirigido a la página principal")

if __name__ == '__main__':
    test_login()

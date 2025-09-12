#!/usr/bin/env python3
"""
Script para crear usuarios de prueba en DuocPoint
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duocpoint.settings.dev')
django.setup()

from django.contrib.auth import get_user_model
from duocpoint.apps.campuses.models import Sede

User = get_user_model()

def create_test_users():
    """Crear usuarios de prueba para desarrollo."""
    
    print("Creando usuarios de prueba...")
    
    # Obtener o crear sede por defecto
    sede, created = Sede.objects.get_or_create(
        nombre="Sede Central",
        defaults={
            'slug': 'sede-central',
            'direccion': 'Av. Ejemplo 123',
            'lat': -33.4489,
            'lng': -70.6693
        }
    )
    
    if created:
        print(f"✅ Sede creada: {sede.nombre}")
    else:
        print(f"✅ Sede encontrada: {sede.nombre}")
    
    # Usuarios de prueba
    test_users = [
        {
            'email': 'admin@duocuc.cl',
            'password': 'admin123',
            'name': 'Administrador DuocPoint',
            'role': 'admin',
            'career': 'Administración',
            'campus': sede,
            'es_estudiante_gmail': False
        },
        {
            'email': 'estudiante@gmail.com',
            'password': 'estudiante123',
            'name': 'Juan Pérez',
            'role': 'student',
            'career': 'Ingeniería en Informática',
            'campus': sede,
            'es_estudiante_gmail': True
        },
        {
            'email': 'profesor@duocuc.cl',
            'password': 'profesor123',
            'name': 'María González',
            'role': 'teacher',
            'career': 'Pedagogía',
            'campus': sede,
            'es_estudiante_gmail': False
        },
        {
            'email': 'moderador@duocuc.cl',
            'password': 'moderador123',
            'name': 'Carlos Rodríguez',
            'role': 'moderator',
            'career': 'Comunicación Social',
            'campus': sede,
            'es_estudiante_gmail': False
        }
    ]
    
    created_count = 0
    updated_count = 0
    
    for user_data in test_users:
        email = user_data['email']
        password = user_data.pop('password')
        
        # Verificar si el usuario ya existe
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            print(f"✅ Usuario actualizado: {email}")
            updated_count += 1
        else:
            # Crear nuevo usuario
            user = User.objects.create_user(
                email=email,
                password=password,
                name=user_data['name'],
                role=user_data['role'],
                career=user_data['career'],
                campus=user_data['campus'],
                es_estudiante_gmail=user_data['es_estudiante_gmail']
            )
            print(f"✅ Usuario creado: {email}")
            created_count += 1
    
    print(f"\n📊 Resumen:")
    print(f"   - Usuarios creados: {created_count}")
    print(f"   - Usuarios actualizados: {updated_count}")
    print(f"   - Total procesados: {created_count + updated_count}")
    
    print(f"\n🔑 Credenciales de prueba:")
    print(f"   - Admin: admin@duocuc.cl / admin123")
    print(f"   - Estudiante: estudiante@gmail.com / estudiante123")
    print(f"   - Profesor: profesor@duocuc.cl / profesor123")
    print(f"   - Moderador: moderador@duocuc.cl / moderador123")

if __name__ == '__main__':
    create_test_users()

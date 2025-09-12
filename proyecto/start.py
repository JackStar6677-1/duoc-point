#!/usr/bin/env python3
"""
DuocPoint - Sistema de Gestión Estudiantil
Iniciador del Sistema

Este script inicia el servidor de desarrollo de DuocPoint.
Sistema integral para la comunidad estudiantil de Duoc UC.

Autor: Equipo DuocPoint
Versión: 1.2.0
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def check_requirements():
    """Verificar que los requisitos estén instalados."""
    try:
        import django
        print(f"Django {django.get_version()} detectado")
    except ImportError:
        print("ERROR: Django no está instalado")
        print("Ejecute: pip install -r proyecto/src/backend/requirements.txt")
        return False
    
    return True

def setup_environment():
    """Configurar variables de entorno."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duocpoint.settings.dev')
    
    # Agregar el directorio del backend al path
    backend_path = Path(__file__).parent / 'src' / 'backend'
    sys.path.insert(0, str(backend_path))

def run_migrations():
    """Ejecutar migraciones de base de datos."""
    print("Ejecutando migraciones de base de datos...")
    try:
        subprocess.run([
            sys.executable, 'manage.py', 'migrate'
        ], cwd='proyecto/src/backend', check=True)
        print("Migraciones completadas")
    except subprocess.CalledProcessError as e:
        print(f"Error en migraciones: {e}")
        return False
    return True

def create_superuser():
    """Crear superusuario si no existe."""
    print("Verificando superusuario...")
    try:
        # Verificar si ya existe un superusuario
        result = subprocess.run([
            sys.executable, 'manage.py', 'shell', '-c',
            'from django.contrib.auth import get_user_model; User = get_user_model(); print("EXISTS" if User.objects.filter(is_superuser=True).exists() else "NOT_EXISTS")'
        ], cwd='proyecto/src/backend', capture_output=True, text=True)
        
        if "NOT_EXISTS" in result.stdout:
            print("Creando superusuario...")
            subprocess.run([
                sys.executable, 'manage.py', 'createsuperuser',
                '--email', 'admin@duocuc.cl',
                '--noinput'
            ], cwd='proyecto/src/backend')
            print("Superusuario creado: admin@duocuc.cl")
        else:
            print("Superusuario ya existe")
    except subprocess.CalledProcessError as e:
        print(f"Error creando superusuario: {e}")

def load_initial_data():
    """Cargar datos iniciales del sistema."""
    print("Cargando datos iniciales...")
    try:
        subprocess.run([
            sys.executable, 'manage.py', 'loaddata', 'initial_data.json'
        ], cwd='proyecto/src/backend', check=False)
        print("Datos iniciales cargados")
    except subprocess.CalledProcessError:
        print("No se encontraron datos iniciales (opcional)")

def get_local_ip():
    """Obtener la IP local de la PC."""
    try:
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except:
        return '127.0.0.1'

def start_server(host='127.0.0.1', port=8000, debug=True):
    """Iniciar el servidor de desarrollo."""
    # Detectar IP local automáticamente
    local_ip = get_local_ip()
    
    print(f"Iniciando servidor en:")
    print(f"  - Local: http://{host}:{port}")
    if local_ip != host:
        print(f"  - Red local: http://{local_ip}:{port}")
    print("Presione Ctrl+C para detener el servidor")
    
    try:
        # Usar 0.0.0.0 para permitir acceso desde la red local
        subprocess.run([
            sys.executable, 'manage.py', 'runserver', f'0.0.0.0:{port}'
        ], cwd='proyecto/src/backend')
    except KeyboardInterrupt:
        print("\nServidor detenido")
    except subprocess.CalledProcessError as e:
        print(f"Error iniciando servidor: {e}")

def main():
    """Función principal."""
    parser = argparse.ArgumentParser(description='Iniciar DuocPoint')
    parser.add_argument('--host', default='127.0.0.1', help='Host del servidor')
    parser.add_argument('--port', type=int, default=8000, help='Puerto del servidor')
    parser.add_argument('--no-migrate', action='store_true', help='Omitir migraciones')
    parser.add_argument('--no-superuser', action='store_true', help='Omitir creación de superusuario')
    parser.add_argument('--no-data', action='store_true', help='Omitir carga de datos iniciales')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("DuocPoint - Sistema de Gestión Estudiantil")
    print("Versión 1.2.0")
    print("=" * 60)
    
    # Verificar requisitos
    if not check_requirements():
        sys.exit(1)
    
    # Configurar entorno
    setup_environment()
    
    # Ejecutar migraciones
    if not args.no_migrate:
        if not run_migrations():
            sys.exit(1)
    
    # Crear superusuario
    if not args.no_superuser:
        create_superuser()
    
    # Cargar datos iniciales
    if not args.no_data:
        load_initial_data()
    
    # Detectar IP local para mostrar URLs de acceso
    local_ip = get_local_ip()
    
    print("\nSistema listo para usar")
    print("Acceso:")
    print(f"  - Aplicación (Local): http://127.0.0.1:{args.port}")
    print(f"  - Aplicación (Red): http://{local_ip}:{args.port}")
    print(f"  - Admin (Local): http://127.0.0.1:{args.port}/admin/")
    print(f"  - Admin (Red): http://{local_ip}:{args.port}/admin/")
    print(f"  - API (Local): http://127.0.0.1:{args.port}/api/")
    print(f"  - API (Red): http://{local_ip}:{args.port}/api/")
    print("\nCredenciales por defecto:")
    print("  - Email: admin@duocuc.cl")
    print("  - Contraseña: admin123")
    print()
    
    # Iniciar servidor
    start_server(args.host, args.port)

if __name__ == '__main__':
    main()

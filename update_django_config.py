#!/usr/bin/env python3
"""
Actualizador de Configuración Django para DuocPoint
Actualiza automáticamente la configuración de Django con la IP local detectada
"""

import os
import re
import socket
from pathlib import Path

def get_local_ip():
    """Obtiene la IP local de la PC."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except:
        return '127.0.0.1'

def update_django_settings(ip):
    """Actualiza la configuración de Django con la IP detectada."""
    settings_file = Path("src/backend/duocpoint/settings/dev.py")
    
    if not settings_file.exists():
        print(f"[WARNING] Archivo de configuración no encontrado: {settings_file}")
        return False
    
    try:
        with open(settings_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Actualizar CSRF_TRUSTED_ORIGINS
        csrf_pattern = r'CSRF_TRUSTED_ORIGINS = \[(.*?)\]'
        csrf_match = re.search(csrf_pattern, content, re.DOTALL)
        
        if csrf_match:
            current_origins = csrf_match.group(1)
            new_origin = f'    "http://{ip}:8000",'
            
            # Verificar si la IP ya está en la lista
            if f'http://{ip}:8000' not in current_origins:
                # Agregar la nueva IP a los orígenes
                updated_origins = current_origins.rstrip() + f',\n{new_origin}'
                content = content.replace(csrf_match.group(0), 
                                        f'CSRF_TRUSTED_ORIGINS = [{updated_origins}\n]')
                print(f"[INFO] Agregada IP {ip} a CSRF_TRUSTED_ORIGINS")
        
        # Actualizar ALLOWED_HOSTS - agregar IP específica si no está
        allowed_hosts_pattern = r'ALLOWED_HOSTS = \[(.*?)\]'
        allowed_hosts_match = re.search(allowed_hosts_pattern, content, re.DOTALL)
        
        if allowed_hosts_match:
            current_hosts = allowed_hosts_match.group(1)
            new_host = f'    "{ip}",'
            
            # Verificar si la IP ya está en la lista
            if f'"{ip}"' not in current_hosts:
                # Agregar la nueva IP a los hosts permitidos
                updated_hosts = current_hosts.rstrip() + f',\n{new_host}'
                content = content.replace(allowed_hosts_match.group(0), 
                                        f'ALLOWED_HOSTS = [{updated_hosts}\n]')
                print(f"[INFO] Agregada IP {ip} a ALLOWED_HOSTS")
        
        # Escribir el archivo actualizado
        with open(settings_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"[SUCCESS] Configuración de Django actualizada con IP: {ip}")
        return True
        
    except Exception as e:
        print(f"[ERROR] No se pudo actualizar la configuración de Django: {e}")
        return False

def update_env_file(ip):
    """Actualiza el archivo .env con la IP detectada."""
    env_file = Path(".env")
    
    env_content = f"""# Configuración de desarrollo local para DuocPoint
# IP detectada automáticamente: {ip}

# Configuración de Django
SECRET_KEY=dev-insecure-key-change-in-production
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,{ip}

# Configuración de base de datos (SQLite para desarrollo)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Configuración de CORS para desarrollo
CORS_ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000,http://0.0.0.0:8000,http://{ip}:8000

# Configuración de Redis (opcional para desarrollo)
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Configuración de email (opcional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=noreply@duocuc.cl

# Configuración de Web Push (opcional)
VAPID_PUBLIC_KEY=
VAPID_PRIVATE_KEY=
VAPID_ADMIN_EMAIL=admin@duocuc.cl

# Modo demo (permite acceso sin autenticación)
DEMO_MODE=0

# IP local detectada automáticamente
LOCAL_IP={ip}
"""
    
    try:
        with open(env_file, "w", encoding="utf-8") as f:
            f.write(env_content)
        print(f"[SUCCESS] Archivo .env actualizado con IP: {ip}")
        return True
    except Exception as e:
        print(f"[ERROR] No se pudo actualizar el archivo .env: {e}")
        return False

def main():
    """Función principal."""
    print("=" * 60)
    print("DuocPoint - Actualizador de Configuración Django")
    print("=" * 60)
    
    # Detectar IP local
    print("[INFO] Detectando IP local...")
    local_ip = get_local_ip()
    print(f"[SUCCESS] IP local detectada: {local_ip}")
    
    # Actualizar configuración
    print("[INFO] Actualizando configuración...")
    
    success = True
    success &= update_env_file(local_ip)
    success &= update_django_settings(local_ip)
    
    if success:
        print("\n" + "=" * 60)
        print("CONFIGURACIÓN ACTUALIZADA EXITOSAMENTE")
        print("=" * 60)
        print(f"IP configurada: {local_ip}")
        print(f"URLs de acceso:")
        print(f"  - Local: http://127.0.0.1:8000")
        print(f"  - Red local: http://{local_ip}:8000")
        print("\nLa aplicación ahora funcionará independientemente en esta PC")
        print("=" * 60)
    else:
        print("\n[ERROR] Hubo problemas actualizando la configuración")
        return False
    
    return True

if __name__ == "__main__":
    main()


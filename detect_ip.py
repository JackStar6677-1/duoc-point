#!/usr/bin/env python3
"""
Detector de IP Local para DuocPoint
Detecta automáticamente la IP local de la PC para configurar el servidor
"""

import socket
import subprocess
import platform
import re
from typing import List, Optional

def get_local_ip() -> Optional[str]:
    """
    Obtiene la IP local de la PC usando múltiples métodos
    """
    try:
        # Método 1: Conectar a un servidor externo para obtener IP local
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            return local_ip
    except Exception:
        pass
    
    try:
        # Método 2: Usar hostname
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        if local_ip != "127.0.0.1":
            return local_ip
    except Exception:
        pass
    
    try:
        # Método 3: Usar comando del sistema operativo
        if platform.system() == "Windows":
            result = subprocess.run(
                ["ipconfig"], 
                capture_output=True, 
                text=True, 
                shell=True
            )
            # Buscar IP en la salida de ipconfig
            lines = result.stdout.split('\n')
            for line in lines:
                if "IPv4" in line and "192.168" in line:
                    ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if ip_match:
                        return ip_match.group(1)
        else:
            # Linux/Mac
            result = subprocess.run(
                ["hostname", "-I"], 
                capture_output=True, 
                text=True
            )
            if result.returncode == 0:
                ips = result.stdout.strip().split()
                for ip in ips:
                    if ip.startswith("192.168") or ip.startswith("10.") or ip.startswith("172."):
                        return ip
    except Exception:
        pass
    
    return None

def get_all_local_ips() -> List[str]:
    """
    Obtiene todas las IPs locales disponibles
    """
    ips = []
    
    # IPs comunes de localhost
    ips.extend(["127.0.0.1", "localhost", "0.0.0.0"])
    
    # Detectar IP principal
    main_ip = get_local_ip()
    if main_ip:
        ips.append(main_ip)
    
    # IPs comunes de red local
    common_ips = [
        "192.168.1.1", "192.168.1.100", "192.168.1.101", "192.168.1.102",
        "192.168.0.1", "192.168.0.100", "192.168.0.101", "192.168.0.102",
        "192.168.100.1", "192.168.100.2", "192.168.100.100",
        "10.0.0.1", "10.0.0.100", "10.0.0.101"
    ]
    
    for ip in common_ips:
        if ip not in ips:
            ips.append(ip)
    
    return ips

def create_env_file(ip: str) -> None:
    """
    Crea o actualiza el archivo .env con la IP detectada
    """
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
    
    with open(".env", "w", encoding="utf-8") as f:
        f.write(env_content)
    
    print(f"[INFO] Archivo .env actualizado con IP: {ip}")

def update_django_settings(ip: str) -> None:
    """
    Actualiza la configuración de Django para incluir la IP detectada
    """
    settings_file = "src/backend/duocpoint/settings/dev.py"
    
    try:
        with open(settings_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Actualizar CSRF_TRUSTED_ORIGINS
        csrf_pattern = r'CSRF_TRUSTED_ORIGINS = \[(.*?)\]'
        csrf_match = re.search(csrf_pattern, content, re.DOTALL)
        
        if csrf_match:
            current_origins = csrf_match.group(1)
            new_origin = f'    "http://{ip}:8000",'
            
            if new_origin not in current_origins:
                # Agregar la nueva IP a los orígenes
                updated_origins = current_origins.rstrip() + f',\n{new_origin}'
                content = content.replace(csrf_match.group(0), 
                                        f'CSRF_TRUSTED_ORIGINS = [{updated_origins}\n]')
        
        # Actualizar ALLOWED_HOSTS
        allowed_hosts_pattern = r'ALLOWED_HOSTS = \[(.*?)\]'
        allowed_hosts_match = re.search(allowed_hosts_pattern, content, re.DOTALL)
        
        if allowed_hosts_match:
            current_hosts = allowed_hosts_match.group(1)
            new_host = f'    "{ip}",'
            
            if new_host not in current_hosts:
                # Agregar la nueva IP a los hosts permitidos
                updated_hosts = current_hosts.rstrip() + f',\n{new_host}'
                content = content.replace(allowed_hosts_match.group(0), 
                                        f'ALLOWED_HOSTS = [{updated_hosts}\n]')
        
        with open(settings_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"[INFO] Configuración de Django actualizada con IP: {ip}")
        
    except Exception as e:
        print(f"[WARNING] No se pudo actualizar la configuración de Django: {e}")

def main():
    """
    Función principal que detecta la IP y actualiza la configuración
    """
    print("=" * 60)
    print("DuocPoint - Detector de IP Local")
    print("=" * 60)
    
    # Detectar IP local
    print("[INFO] Detectando IP local...")
    local_ip = get_local_ip()
    
    if local_ip:
        print(f"[SUCCESS] IP local detectada: {local_ip}")
    else:
        print("[WARNING] No se pudo detectar IP local, usando 127.0.0.1")
        local_ip = "127.0.0.1"
    
    # Mostrar todas las IPs disponibles
    all_ips = get_all_local_ips()
    print(f"[INFO] IPs disponibles: {', '.join(all_ips[:5])}...")
    
    # Actualizar archivos de configuración
    print("[INFO] Actualizando configuración...")
    create_env_file(local_ip)
    update_django_settings(local_ip)
    
    print("\n" + "=" * 60)
    print("CONFIGURACIÓN COMPLETADA")
    print("=" * 60)
    print(f"IP principal: {local_ip}")
    print(f"URLs de acceso:")
    print(f"  - Local: http://127.0.0.1:8000")
    print(f"  - Red local: http://{local_ip}:8000")
    print(f"  - Otros dispositivos: http://{local_ip}:8000")
    print("\nLa aplicación ahora funcionará independientemente en esta PC")
    print("=" * 60)
    
    return local_ip

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script de diagnóstico de red para DuocPoint
"""

import socket
import subprocess
import sys
import os
from pathlib import Path

def get_local_ip():
    """Obtiene la IP local de la PC."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except:
        return '127.0.0.1'

def check_port_available(port=8000):
    """Verifica si el puerto está disponible."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('127.0.0.1', port))
            return True
    except OSError:
        return False

def check_django_config():
    """Verifica la configuración de Django."""
    try:
        backend_path = Path("src/backend")
        if not backend_path.exists():
            return False, "Directorio del backend no encontrado"
        
        result = subprocess.run([
            sys.executable, "manage.py", "check", "--settings=duocpoint.settings.dev"
        ], cwd=backend_path, capture_output=True, text=True)
        
        if result.returncode == 0:
            return True, "Configuración válida"
        else:
            return False, f"Error: {result.stderr}"
            
    except Exception as e:
        return False, f"Error: {e}"

def test_server_connection(ip, port=8000):
    """Prueba la conexión al servidor."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            result = s.connect_ex((ip, port))
            return result == 0
    except:
        return False

def main():
    """Función principal de diagnóstico."""
    print("=" * 60)
    print("DuocPoint - Diagnóstico de Red")
    print("=" * 60)
    
    # Detectar IP local
    local_ip = get_local_ip()
    print(f"IP local detectada: {local_ip}")
    
    # Verificar puerto
    port_available = check_port_available()
    print(f"Puerto 8000 disponible: {'✅ SÍ' if port_available else '❌ NO'}")
    
    # Verificar configuración Django
    config_ok, config_msg = check_django_config()
    print(f"Configuración Django: {'✅ OK' if config_ok else '❌ ERROR'}")
    if not config_ok:
        print(f"  Detalle: {config_msg}")
    
    # Verificar archivo .env
    env_file = Path(".env")
    if env_file.exists():
        print("✅ Archivo .env encontrado")
        with open(env_file, 'r') as f:
            content = f.read()
            if local_ip in content:
                print(f"✅ IP {local_ip} configurada en .env")
            else:
                print(f"❌ IP {local_ip} NO configurada en .env")
    else:
        print("❌ Archivo .env no encontrado")
    
    # Verificar configuración de Django
    settings_file = Path("src/backend/duocpoint/settings/dev.py")
    if settings_file.exists():
        with open(settings_file, 'r') as f:
            content = f.read()
            if local_ip in content:
                print(f"✅ IP {local_ip} configurada en settings/dev.py")
            else:
                print(f"❌ IP {local_ip} NO configurada en settings/dev.py")
    
    print("\n" + "=" * 60)
    print("URLs de prueba:")
    print("=" * 60)
    print(f"Local: http://127.0.0.1:8000")
    print(f"Red local: http://{local_ip}:8000")
    
    # Probar conexiones
    print("\nProbando conexiones...")
    local_ok = test_server_connection('127.0.0.1')
    network_ok = test_server_connection(local_ip)
    
    print(f"Local (127.0.0.1): {'✅ OK' if local_ok else '❌ NO RESPONDE'}")
    print(f"Red local ({local_ip}): {'✅ OK' if network_ok else '❌ NO RESPONDE'}")
    
    if not local_ok and not network_ok:
        print("\n⚠️  El servidor no está corriendo o no responde")
        print("Ejecuta: iniciar_desarrollo.bat")
    elif local_ok and not network_ok:
        print(f"\n⚠️  El servidor solo responde localmente")
        print("Verifica la configuración de red o firewall")
    elif not local_ok and network_ok:
        print(f"\n⚠️  El servidor responde en red pero no localmente")
        print("Esto es inusual, verifica la configuración")
    else:
        print(f"\n✅ El servidor responde correctamente en ambas direcciones")
    
    print("=" * 60)

if __name__ == "__main__":
    main()

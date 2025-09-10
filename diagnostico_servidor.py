#!/usr/bin/env python3
"""
Diagnóstico avanzado del servidor DuocPoint
"""

import socket
import subprocess
import sys
import time
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

def check_port_status(host, port):
    """Verifica el estado de un puerto."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            result = s.connect_ex((host, port))
            return result == 0
    except:
        return False

def check_django_process():
    """Verifica si hay procesos de Django corriendo."""
    try:
        result = subprocess.run(
            ["tasklist", "/FI", "IMAGENAME eq python.exe"],
            capture_output=True, text=True, shell=True
        )
        return "python.exe" in result.stdout
    except:
        return False

def test_http_connection(host, port):
    """Prueba una conexión HTTP real."""
    try:
        import urllib.request
        import urllib.error
        
        url = f"http://{host}:{port}/"
        request = urllib.request.Request(url)
        request.add_header('User-Agent', 'DuocPoint-Diagnostic/1.0')
        
        with urllib.request.urlopen(request, timeout=5) as response:
            return response.status == 200, response.status
    except urllib.error.HTTPError as e:
        return False, e.code
    except Exception as e:
        return False, str(e)

def check_django_config():
    """Verifica la configuración de Django."""
    try:
        backend_path = Path("src/backend")
        if not backend_path.exists():
            return False, "Directorio backend no encontrado"
        
        # Verificar que manage.py existe
        manage_py = backend_path / "manage.py"
        if not manage_py.exists():
            return False, "manage.py no encontrado"
        
        # Verificar configuración
        result = subprocess.run([
            sys.executable, "manage.py", "check", "--settings=duocpoint.settings.dev"
        ], cwd=backend_path, capture_output=True, text=True)
        
        if result.returncode == 0:
            return True, "Configuración válida"
        else:
            return False, f"Error de configuración: {result.stderr}"
            
    except Exception as e:
        return False, f"Error: {e}"

def start_test_server():
    """Inicia un servidor de prueba."""
    try:
        backend_path = Path("src/backend")
        
        print("🚀 Iniciando servidor de prueba...")
        
        # Iniciar servidor en background
        process = subprocess.Popen([
            sys.executable, "manage.py", "runserver", "0.0.0.0:8000",
            "--settings=duocpoint.settings.dev"
        ], cwd=backend_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Esperar a que inicie
        time.sleep(5)
        
        # Verificar si está corriendo
        if process.poll() is None:
            print("✅ Servidor iniciado correctamente")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Error iniciando servidor: {stderr.decode()}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    """Función principal de diagnóstico."""
    print("=" * 60)
    print("DuocPoint - Diagnóstico Avanzado del Servidor")
    print("=" * 60)
    
    local_ip = get_local_ip()
    print(f"IP local detectada: {local_ip}")
    
    # Verificar configuración Django
    print("\n🔧 Verificando configuración Django...")
    config_ok, config_msg = check_django_config()
    print(f"Configuración: {'✅ OK' if config_ok else '❌ ERROR'}")
    if not config_ok:
        print(f"Detalle: {config_msg}")
        return
    
    # Verificar procesos Python
    print("\n🐍 Verificando procesos Python...")
    python_running = check_django_process()
    print(f"Procesos Python: {'✅ Detectados' if python_running else '❌ No detectados'}")
    
    # Verificar puertos
    print("\n🔌 Verificando puertos...")
    local_port = check_port_status('127.0.0.1', 8000)
    network_port = check_port_status(local_ip, 8000)
    
    print(f"Puerto 127.0.0.1:8000: {'✅ Abierto' if local_port else '❌ Cerrado'}")
    print(f"Puerto {local_ip}:8000: {'✅ Abierto' if network_port else '❌ Cerrado'}")
    
    # Probar conexiones HTTP
    print("\n🌐 Probando conexiones HTTP...")
    
    if local_port:
        local_http, local_status = test_http_connection('127.0.0.1', 8000)
        print(f"HTTP 127.0.0.1:8000: {'✅ OK' if local_http else '❌ ERROR'} (Status: {local_status})")
    
    if network_port:
        network_http, network_status = test_http_connection(local_ip, 8000)
        print(f"HTTP {local_ip}:8000: {'✅ OK' if network_http else '❌ ERROR'} (Status: {network_status})")
    
    # Si no hay servidor corriendo, intentar iniciarlo
    if not local_port and not network_port:
        print("\n🚀 No hay servidor corriendo, iniciando servidor de prueba...")
        process = start_test_server()
        
        if process:
            print("⏳ Esperando 3 segundos para que el servidor esté listo...")
            time.sleep(3)
            
            # Probar nuevamente
            local_http, local_status = test_http_connection('127.0.0.1', 8000)
            print(f"HTTP 127.0.0.1:8000: {'✅ OK' if local_http else '❌ ERROR'} (Status: {local_status})")
            
            if local_http:
                print(f"\n🎉 ¡Servidor funcionando!")
                print(f"URLs de acceso:")
                print(f"  - Local: http://127.0.0.1:8000")
                print(f"  - Red: http://{local_ip}:8000")
                
                # Terminar el proceso de prueba
                process.terminate()
                process.wait()
            else:
                print("❌ El servidor no responde correctamente")
                if process:
                    process.terminate()
                    process.wait()
    
    print("\n" + "=" * 60)
    print("Diagnóstico completado")
    print("=" * 60)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script de Prueba para Verificar Configuración de DuocPoint
Verifica que la aplicación funcione correctamente con la IP detectada
"""

import os
import sys
import socket
import subprocess
import time
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
        # Cambiar al directorio del backend
        backend_path = Path("src/backend")
        if not backend_path.exists():
            print("[ERROR] Directorio del backend no encontrado")
            return False
        
        # Verificar que manage.py existe
        manage_py = backend_path / "manage.py"
        if not manage_py.exists():
            print("[ERROR] manage.py no encontrado")
            return False
        
        # Verificar configuración de Django
        result = subprocess.run([
            sys.executable, "manage.py", "check", "--settings=duocpoint.settings.dev"
        ], cwd=backend_path, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("[SUCCESS] Configuración de Django válida")
            return True
        else:
            print(f"[ERROR] Configuración de Django inválida: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Error verificando configuración de Django: {e}")
        return False

def check_database():
    """Verifica la base de datos."""
    try:
        backend_path = Path("src/backend")
        
        # Verificar migraciones
        result = subprocess.run([
            sys.executable, "manage.py", "showmigrations", "--settings=duocpoint.settings.dev"
        ], cwd=backend_path, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("[SUCCESS] Base de datos configurada correctamente")
            return True
        else:
            print(f"[WARNING] Problemas con la base de datos: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Error verificando base de datos: {e}")
        return False

def test_server_startup():
    """Prueba el inicio del servidor."""
    try:
        backend_path = Path("src/backend")
        local_ip = get_local_ip()
        
        print(f"[INFO] Probando inicio del servidor en {local_ip}:8000...")
        
        # Iniciar servidor en background
        process = subprocess.Popen([
            sys.executable, "manage.py", "runserver", "0.0.0.0:8000", 
            "--settings=duocpoint.settings.dev"
        ], cwd=backend_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Esperar un poco para que el servidor inicie
        time.sleep(3)
        
        # Verificar si el proceso sigue corriendo
        if process.poll() is None:
            print("[SUCCESS] Servidor iniciado correctamente")
            
            # Intentar conectar al servidor
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(5)
                    result = s.connect_ex(('127.0.0.1', 8000))
                    if result == 0:
                        print("[SUCCESS] Servidor responde en localhost:8000")
                    else:
                        print("[WARNING] Servidor no responde en localhost:8000")
            except Exception as e:
                print(f"[WARNING] Error conectando al servidor: {e}")
            
            # Terminar el proceso
            process.terminate()
            process.wait()
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"[ERROR] Servidor no pudo iniciar: {stderr.decode()}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Error probando inicio del servidor: {e}")
        return False

def main():
    """Función principal de prueba."""
    print("=" * 60)
    print("DuocPoint - Prueba de Configuración")
    print("=" * 60)
    
    # Detectar IP local
    local_ip = get_local_ip()
    print(f"[INFO] IP local detectada: {local_ip}")
    
    # Verificaciones
    tests = [
        ("Puerto 8000 disponible", lambda: check_port_available()),
        ("Configuración de Django", check_django_config),
        ("Base de datos", check_database),
        ("Inicio del servidor", test_server_startup),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n[TEST] {test_name}...")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"[ERROR] Error en {test_name}: {e}")
            results.append((test_name, False))
    
    # Resumen de resultados
    print("\n" + "=" * 60)
    print("RESUMEN DE PRUEBAS")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\nResultado: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("\n🎉 ¡Todas las pruebas pasaron!")
        print("La aplicación está configurada correctamente para esta PC")
        print(f"\nURLs de acceso:")
        print(f"  - Local: http://127.0.0.1:8000")
        print(f"  - Red local: http://{local_ip}:8000")
    else:
        print(f"\n⚠️  {total - passed} pruebas fallaron")
        print("Revisa la configuración antes de continuar")
    
    print("=" * 60)
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

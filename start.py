#!/usr/bin/env python
"""
🚀 DuocPoint - Script Maestro de Inicio
=====================================

Este script maneja todo el inicio de DuocPoint:
- Servidor Django
- PWA con HTTPS (ngrok)
- Acceso en red local
- Verificación de dependencias

Uso:
    python start.py [opción]

Opciones:
    local       - Solo localhost (PWA completo)
    network     - Red local (192.168.x.x)
    ngrok       - Con ngrok HTTPS (PWA completo en móvil)
    all         - Todos los métodos (por defecto)
    test        - Solo tests
"""

import subprocess
import sys
import os
import time
import threading
import webbrowser
import requests
from pathlib import Path

class DuocPointLauncher:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.server_dir = self.base_dir / "server"
        self.web_dir = self.base_dir / "web"
        self.processes = []
        
    def print_banner(self):
        """Mostrar banner de DuocPoint"""
        print("=" * 60)
        print("🎓 DuocPoint - Plataforma Integral Duoc UC")
        print("=" * 60)
        print("🚀 Iniciando servidor...")
        print()
        
    def check_dependencies(self):
        """Verificar dependencias"""
        print("🔍 Verificando dependencias...")
        
        # Verificar Python
        if sys.version_info < (3, 8):
            print("❌ Python 3.8+ requerido")
            return False
            
        # Verificar Django
        try:
            import django
            print(f"✅ Django {django.get_version()}")
        except ImportError:
            print("❌ Django no instalado")
            return False
            
        # Verificar ngrok (opcional)
        try:
            result = subprocess.run(['ngrok', 'version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("✅ ngrok disponible")
                self.ngrok_available = True
            else:
                print("⚠️ ngrok no disponible (opcional)")
                self.ngrok_available = False
        except:
            print("⚠️ ngrok no disponible (opcional)")
            self.ngrok_available = False
            
        return True
        
    def start_django_server(self, host="localhost", port=8000):
        """Iniciar servidor Django"""
        print(f"🚀 Iniciando servidor Django en {host}:{port}...")
        
        try:
            os.chdir(self.server_dir)
            process = subprocess.Popen([
                sys.executable, 'manage.py', 'runserver', f'{host}:{port}'
            ])
            self.processes.append(process)
            
            # Esperar a que el servidor inicie
            time.sleep(3)
            
            # Verificar que el servidor esté corriendo
            try:
                response = requests.get(f'http://{host}:{port}/', timeout=5)
                if response.status_code == 200:
                    print(f"✅ Servidor Django iniciado en http://{host}:{port}")
                    return True
            except:
                pass
                
            print(f"⚠️ Servidor iniciado en http://{host}:{port}")
            return True
            
        except Exception as e:
            print(f"❌ Error iniciando servidor: {e}")
            return False
            
    def start_ngrok(self, port=8000):
        """Iniciar ngrok para HTTPS"""
        if not self.ngrok_available:
            print("❌ ngrok no disponible")
            return None
            
        print("🌐 Iniciando ngrok...")
        
        try:
            process = subprocess.Popen(['ngrok', 'http', str(port)])
            self.processes.append(process)
            
            # Esperar a que ngrok inicie
            time.sleep(5)
            
            # Obtener URL de ngrok
            try:
                response = requests.get('http://localhost:4040/api/tunnels', timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    if data['tunnels']:
                        ngrok_url = data['tunnels'][0]['public_url']
                        print(f"✅ ngrok iniciado: {ngrok_url}")
                        return ngrok_url
            except:
                pass
                
            print("⚠️ ngrok iniciado (verifica en http://localhost:4040)")
            return "https://xxxxx.ngrok.io"
            
        except Exception as e:
            print(f"❌ Error iniciando ngrok: {e}")
            return None
            
    def get_local_ip(self):
        """Obtener IP local"""
        try:
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "192.168.1.100"
            
    def run_tests(self):
        """Ejecutar tests"""
        print("🧪 Ejecutando tests...")
        
        try:
            os.chdir(self.server_dir)
            result = subprocess.run([
                sys.executable, 'manage.py', 'test', '--verbosity=2'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Tests pasaron")
            else:
                print("⚠️ Algunos tests fallaron")
                print(result.stdout)
                
        except Exception as e:
            print(f"❌ Error ejecutando tests: {e}")
            
    def show_urls(self, ngrok_url=None):
        """Mostrar URLs disponibles"""
        print("\n" + "=" * 60)
        print("🌐 URLs DISPONIBLES:")
        print("=" * 60)
        
        print("💻 LOCAL (PWA completo):")
        print("   http://localhost:8000/")
        print("   http://127.0.0.1:8000/")
        
        local_ip = self.get_local_ip()
        print(f"\n📱 RED LOCAL (PWA limitado):")
        print(f"   http://{local_ip}:8000/")
        
        if ngrok_url:
            print(f"\n🌍 HTTPS (PWA completo en móvil):")
            print(f"   {ngrok_url}")
            
        print(f"\n🧪 TESTS:")
        print(f"   http://localhost:8000/test-all.html")
        print(f"   http://localhost:8000/test-pwa.html")
        
        print(f"\n🔐 LOGIN:")
        print(f"   http://localhost:8000/login.html")
        print(f"   Email: student@duocuc.cl")
        print(f"   Password: student123")
        
        print("\n" + "=" * 60)
        print("📱 PARA PWA EN MÓVIL:")
        print("   1. Usa la URL HTTPS de ngrok")
        print("   2. O conecta tu móvil a la misma red WiFi")
        print("   3. Ve a la URL de red local")
        print("=" * 60)
        
    def cleanup(self):
        """Limpiar procesos"""
        print("\n🛑 Deteniendo servidores...")
        for process in self.processes:
            try:
                process.terminate()
                process.wait(timeout=5)
            except:
                try:
                    process.kill()
                except:
                    pass
        print("✅ Servidores detenidos")
        
    def run(self, mode="all"):
        """Ejecutar DuocPoint"""
        self.print_banner()
        
        # Verificar dependencias
        if not self.check_dependencies():
            return False
            
        try:
            if mode == "test":
                self.run_tests()
                return True
                
            # Iniciar servidor Django
            if not self.start_django_server():
                return False
                
            ngrok_url = None
            
            if mode in ["all", "ngrok"]:
                ngrok_url = self.start_ngrok()
                
            # Mostrar URLs
            self.show_urls(ngrok_url)
            
            # Abrir navegador
            try:
                webbrowser.open('http://localhost:8000/')
            except:
                pass
                
            print("\n⏳ Presiona Ctrl+C para detener...")
            
            # Mantener corriendo
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pass
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            self.cleanup()
            
        return True

def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='DuocPoint Launcher')
    parser.add_argument('mode', nargs='?', default='all',
                       choices=['local', 'network', 'ngrok', 'all', 'test'],
                       help='Modo de ejecución')
    
    args = parser.parse_args()
    
    launcher = DuocPointLauncher()
    success = launcher.run(args.mode)
    
    if success:
        print("🎉 DuocPoint ejecutado exitosamente!")
    else:
        print("❌ Error ejecutando DuocPoint")
        sys.exit(1)

if __name__ == "__main__":
    main()

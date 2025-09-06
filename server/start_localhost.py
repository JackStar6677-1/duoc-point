#!/usr/bin/env python
"""
Script para iniciar el servidor en localhost para PWA
"""

import subprocess
import sys
import os

def start_localhost_server():
    """Iniciar servidor en localhost para PWA"""
    
    print("🚀 Iniciando servidor en localhost para PWA...")
    print("📱 Para PWA en móvil, usa ngrok o similar para HTTPS")
    print("🌐 URLs disponibles:")
    print("   - http://localhost:8000/ (PWA funcionará)")
    print("   - http://127.0.0.1:8000/ (PWA funcionará)")
    print("   - http://192.168.100.2:8000/ (PWA limitado)")
    print()
    
    try:
        # Cambiar al directorio del servidor
        os.chdir('server')
        
        # Iniciar servidor en localhost
        subprocess.run([
            sys.executable, 'manage.py', 'runserver', 'localhost:8000'
        ])
        
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    start_localhost_server()

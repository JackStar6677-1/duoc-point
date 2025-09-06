#!/usr/bin/env python
"""
Script para iniciar servidor con ngrok para PWA HTTPS
"""

import subprocess
import sys
import os
import time
import threading

def start_django_server():
    """Iniciar servidor Django en background"""
    print("🚀 Iniciando servidor Django...")
    try:
        subprocess.run([
            sys.executable, 'manage.py', 'runserver', 'localhost:8000'
        ])
    except Exception as e:
        print(f"❌ Error Django: {e}")

def start_ngrok():
    """Iniciar ngrok para HTTPS"""
    print("🌐 Iniciando ngrok...")
    try:
        subprocess.run(['ngrok', 'http', '8000'])
    except Exception as e:
        print(f"❌ Error ngrok: {e}")
        print("💡 Instala ngrok: https://ngrok.com/download")

def main():
    """Función principal"""
    print("🔧 DuocPoint PWA con HTTPS")
    print("=" * 40)
    
    # Verificar si ngrok está instalado
    try:
        subprocess.run(['ngrok', 'version'], capture_output=True, check=True)
        print("✅ ngrok encontrado")
    except:
        print("❌ ngrok no encontrado")
        print("💡 Instala ngrok: https://ngrok.com/download")
        print("🔄 Iniciando solo servidor Django...")
        
        # Solo iniciar Django
        os.chdir('server')
        start_django_server()
        return
    
    # Cambiar al directorio del servidor
    os.chdir('server')
    
    # Iniciar Django en thread separado
    django_thread = threading.Thread(target=start_django_server)
    django_thread.daemon = True
    django_thread.start()
    
    # Esperar un poco para que Django inicie
    time.sleep(3)
    
    print("✅ Servidor Django iniciado")
    print("🌐 Iniciando ngrok...")
    print("📱 Usa la URL HTTPS de ngrok en tu móvil para PWA completo")
    
    # Iniciar ngrok
    start_ngrok()

if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""
🔒 DuocPoint - Iniciar con Tailscale
===================================

Script específico para iniciar DuocPoint con Tailscale.
Tailscale proporciona HTTPS automáticamente, perfecto para PWA en móvil.

Uso:
    python start_tailscale.py
"""

import subprocess
import sys
import os
import time
import webbrowser
import requests
from pathlib import Path

def check_tailscale():
    """Verificar si Tailscale está instalado y funcionando"""
    try:
        result = subprocess.run(['tailscale', 'status'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return True
    except:
        pass
    return False

def get_tailscale_ip():
    """Obtener IP de Tailscale"""
    try:
        result = subprocess.run(['tailscale', 'ip', '-4'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    return None

def start_django_server():
    """Iniciar servidor Django"""
    print("🚀 Iniciando servidor Django...")
    
    server_dir = Path(__file__).parent / "server"
    os.chdir(server_dir)
    
    try:
        process = subprocess.Popen([
            sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'
        ])
        
        # Esperar a que el servidor inicie
        time.sleep(3)
        
        print("✅ Servidor Django iniciado")
        return process
        
    except Exception as e:
        print(f"❌ Error iniciando servidor: {e}")
        return None

def main():
    """Función principal"""
    print("=" * 60)
    print("🔒 DuocPoint - Iniciar con Tailscale")
    print("=" * 60)
    
    # Verificar Tailscale
    if not check_tailscale():
        print("❌ Tailscale no está instalado o no está funcionando")
        print("💡 Instala Tailscale: https://tailscale.com/download")
        print("💡 O usa: python start.py local")
        return False
    
    # Obtener IP de Tailscale
    tailscale_ip = get_tailscale_ip()
    if not tailscale_ip:
        print("❌ No se pudo obtener la IP de Tailscale")
        print("💡 Verifica que Tailscale esté conectado")
        return False
    
    print(f"✅ Tailscale detectado: {tailscale_ip}")
    
    # Iniciar servidor Django
    process = start_django_server()
    if not process:
        return False
    
    # Mostrar URLs
    print("\n" + "=" * 60)
    print("🌐 URLs DISPONIBLES:")
    print("=" * 60)
    
    print("💻 LOCAL:")
    print("   http://localhost:8000/")
    print("   http://127.0.0.1:8000/")
    
    print(f"\n🔒 TAILSCALE (PWA completo - HTTPS):")
    print(f"   https://{tailscale_ip}:8000/")
    print("   ✅ PWA funcionará perfectamente en móvil")
    
    print(f"\n🧪 TESTS:")
    print(f"   https://{tailscale_ip}:8000/test-all.html")
    print(f"   https://{tailscale_ip}:8000/test-pwa.html")
    
    print(f"\n🔐 LOGIN:")
    print(f"   https://{tailscale_ip}:8000/login.html")
    print(f"   Email: student@duocuc.cl")
    print(f"   Password: student123")
    
    print("\n" + "=" * 60)
    print("📱 PARA PWA EN MÓVIL:")
    print(f"   1. Ve a https://{tailscale_ip}:8000/ en tu móvil")
    print("   2. Deberías ver 'Instalar App'")
    print("   3. La app se instalará como aplicación nativa")
    print("   4. Aparecerá en tu escritorio con el icono de DuocPoint")
    print("=" * 60)
    
    # Abrir navegador
    try:
        webbrowser.open(f'https://{tailscale_ip}:8000/')
    except:
        pass
    
    print("\n⏳ Presiona Ctrl+C para detener...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Deteniendo servidor...")
        process.terminate()
        process.wait()
        print("✅ Servidor detenido")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)

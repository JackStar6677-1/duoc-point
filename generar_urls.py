#!/usr/bin/env python3
"""
Generador de URLs de acceso para DuocPoint
Crea un archivo con todas las URLs de acceso para facilitar el uso
"""

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

def generate_urls_file():
    """Genera un archivo con todas las URLs de acceso."""
    local_ip = get_local_ip()
    
    urls_content = f"""# DuocPoint - URLs de Acceso
# IP local detectada: {local_ip}
# Generado automáticamente

## 🏠 Acceso Local (Siempre disponible)
- **Aplicación Principal**: http://127.0.0.1:8000
- **Panel de Administración**: http://127.0.0.1:8000/admin/
- **API REST**: http://127.0.0.1:8000/api/
- **Documentación API**: http://127.0.0.1:8000/api/docs/

## 🌍 Acceso desde Red Local
- **Aplicación Principal**: http://{local_ip}:8000
- **Panel de Administración**: http://{local_ip}:8000/admin/
- **API REST**: http://{local_ip}:8000/api/
- **Documentación API**: http://{local_ip}:8000/api/docs/

## 📱 Acceso desde Otros Dispositivos
Para acceder desde móviles, tablets u otras PCs en la misma red:
- Usa las URLs de "Red Local" mostradas arriba
- Asegúrate de estar conectado a la misma red WiFi

## 👤 Credenciales de Acceso
- **Email**: admin@duocuc.cl
- **Contraseña**: admin123

## 🔧 Información Técnica
- **Puerto**: 8000
- **IP Local**: {local_ip}
- **Modo**: Desarrollo
- **Base de datos**: SQLite
- **Servidor**: Django Development Server

## 📝 Notas
- Las URLs locales (127.0.0.1) solo funcionan en la PC donde está corriendo el servidor
- Las URLs de red local ({local_ip}) funcionan desde cualquier dispositivo en la misma red
- Si cambias de red, la IP puede cambiar automáticamente
- Para detener el servidor, presiona Ctrl+C en la ventana del terminal

---
Generado automáticamente por DuocPoint
"""
    
    # Escribir archivo de URLs
    urls_file = Path("URLS_ACCESO.txt")
    with open(urls_file, 'w', encoding='utf-8') as f:
        f.write(urls_content)
    
    print(f"✅ Archivo de URLs generado: {urls_file}")
    print(f"📋 IP local: {local_ip}")
    print(f"🔗 URL principal: http://{local_ip}:8000")
    
    return local_ip

def main():
    """Función principal."""
    print("=" * 60)
    print("DuocPoint - Generador de URLs de Acceso")
    print("=" * 60)
    
    local_ip = generate_urls_file()
    
    print("\n" + "=" * 60)
    print("URLs principales:")
    print("=" * 60)
    print(f"🏠 Local: http://127.0.0.1:8000")
    print(f"🌍 Red: http://{local_ip}:8000")
    print("=" * 60)

if __name__ == "__main__":
    main()

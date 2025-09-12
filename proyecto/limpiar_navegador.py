#!/usr/bin/env python3
"""
Script para limpiar cache y cookies del navegador para DuocPoint
"""

import os
import subprocess
import sys
import webbrowser
from pathlib import Path

def clear_browser_cache():
    """Limpia el cache del navegador."""
    print("🧹 Limpiando cache del navegador...")
    
    # Limpiar cache de Chrome
    try:
        chrome_cache = Path.home() / "AppData/Local/Google/Chrome/User Data/Default/Cache"
        if chrome_cache.exists():
            subprocess.run(["rmdir", "/s", "/q", str(chrome_cache)], shell=True, capture_output=True)
            print("✅ Cache de Chrome limpiado")
    except:
        print("⚠️  No se pudo limpiar cache de Chrome")
    
    # Limpiar cache de Edge
    try:
        edge_cache = Path.home() / "AppData/Local/Microsoft/Edge/User Data/Default/Cache"
        if edge_cache.exists():
            subprocess.run(["rmdir", "/s", "/q", str(edge_cache)], shell=True, capture_output=True)
            print("✅ Cache de Edge limpiado")
    except:
        print("⚠️  No se pudo limpiar cache de Edge")
    
    # Limpiar cache de Firefox
    try:
        firefox_cache = Path.home() / "AppData/Local/Mozilla/Firefox/Profiles"
        if firefox_cache.exists():
            for profile in firefox_cache.glob("*/cache2"):
                subprocess.run(["rmdir", "/s", "/q", str(profile)], shell=True, capture_output=True)
            print("✅ Cache de Firefox limpiado")
    except:
        print("⚠️  No se pudo limpiar cache de Firefox")

def clear_dns_cache():
    """Limpia el cache DNS."""
    print("🌐 Limpiando cache DNS...")
    try:
        subprocess.run(["ipconfig", "/flushdns"], shell=True, capture_output=True)
        print("✅ Cache DNS limpiado")
    except:
        print("⚠️  No se pudo limpiar cache DNS")

def open_browser_clean(url):
    """Abre el navegador en modo incógnito."""
    print(f"🌐 Abriendo navegador en modo incógnito: {url}")
    
    try:
        # Intentar abrir en modo incógnito
        webbrowser.open_new(url)
        print("✅ Navegador abierto")
    except Exception as e:
        print(f"⚠️  Error abriendo navegador: {e}")

def main():
    """Función principal."""
    print("=" * 60)
    print("DuocPoint - Limpieza de Navegador")
    print("=" * 60)
    
    # Limpiar cache
    clear_browser_cache()
    clear_dns_cache()
    
    print("\n" + "=" * 60)
    print("Limpieza completada")
    print("=" * 60)
    print("💡 Recomendaciones:")
    print("1. Cierra todos los navegadores")
    print("2. Reinicia el navegador")
    print("3. Prueba en modo incógnito")
    print("4. Si persiste el problema, reinicia la PC")
    print("=" * 60)

if __name__ == "__main__":
    main()

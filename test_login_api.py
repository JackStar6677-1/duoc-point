#!/usr/bin/env python3
"""
Script para probar la API de login
"""

import requests
import json

def test_login():
    """Prueba el endpoint de login"""
    url = "http://127.0.0.1:8000/api/auth/login/"
    
    # Datos de prueba
    test_data = {
        "email": "estudiante@gmail.com",
        "password": "estudiante123"
    }
    
    try:
        print("🔍 Probando login con:", test_data["email"])
        
        response = requests.post(
            url,
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"📊 Status Code: {response.status_code}")
        print(f"📋 Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Login exitoso!")
            print(f"🔑 Access Token: {data.get('access', 'N/A')[:50]}...")
            print(f"👤 Usuario: {data.get('user', {}).get('name', 'N/A')}")
            return True
        else:
            print("❌ Error en login:")
            print(f"📄 Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar al servidor")
        print("💡 Asegúrate de que el servidor Django esté corriendo en http://127.0.0.1:8000")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def test_logo_access():
    """Prueba el acceso al logo"""
    url = "http://127.0.0.1:8000/imagenes/logos-iconos/Logo_DuocUC.svg.png"
    
    try:
        print("\n🖼️ Probando acceso al logo...")
        
        response = requests.get(url)
        
        print(f"📊 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Logo accesible!")
            print(f"📏 Tamaño: {len(response.content)} bytes")
            return True
        else:
            print("❌ Logo no accesible:")
            print(f"📄 Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar al servidor")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Pruebas de API DuocPoint")
    print("=" * 50)
    
    # Probar login
    login_ok = test_login()
    
    # Probar logo
    logo_ok = test_logo_access()
    
    print("\n📊 Resumen:")
    print(f"   Login: {'✅ OK' if login_ok else '❌ FALLO'}")
    print(f"   Logo:  {'✅ OK' if logo_ok else '❌ FALLO'}")
    
    if login_ok and logo_ok:
        print("\n🎉 Todas las pruebas pasaron!")
    else:
        print("\n⚠️ Algunas pruebas fallaron. Revisa los errores arriba.")

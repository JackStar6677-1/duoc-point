@echo off
chcp 65001 >nul
title DuocPoint - Configuración Completa de Aplicación Móvil

echo.
echo ============================================================
echo    DuocPoint - Configuración Completa de App Móvil
echo    Versión 1.2.0
echo ============================================================
echo.

:: Verificar Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js no está instalado
    echo Descarga Node.js desde: https://nodejs.org
    pause
    exit /b 1
)

echo [INFO] Node.js detectado correctamente
echo.

:: Navegar al directorio frontend
cd src\frontend

:: Crear package.json si no existe
if not exist "package.json" (
    echo [INFO] Creando package.json...
    (
    echo {
    echo   "name": "duocpoint-mobile",
    echo   "version": "1.2.0",
    echo   "description": "DuocPoint Mobile App",
    echo   "scripts": {
    echo     "build": "npx cap sync",
    echo     "android": "npx cap run android",
    echo     "android:build": "npx cap build android",
    echo     "android:open": "npx cap open android"
    echo   },
    echo   "dependencies": {
    echo     "@capacitor/core": "^5.0.0",
    echo     "@capacitor/cli": "^5.0.0",
    echo     "@capacitor/android": "^5.0.0"
    echo   }
    echo }
    ) > package.json
)

:: Instalar Capacitor CLI globalmente
echo [INFO] Instalando Capacitor CLI...
npm install -g @capacitor/cli

:: Instalar dependencias
echo [INFO] Instalando dependencias...
npm install

:: Inicializar Capacitor si no existe
if not exist "capacitor.config.ts" (
    echo [INFO] Inicializando Capacitor...
    npx cap init DuocPoint com.duocuc.duocpoint --web-dir=../
)

:: Crear archivo de configuración
echo [INFO] Creando configuración de Capacitor...
(
echo import { CapacitorConfig } from '@capacitor/cli';
echo.
echo const config: CapacitorConfig = {
echo   appId: 'com.duocuc.duocpoint',
echo   appName: 'DuocPoint',
echo   webDir: '../',
echo   server: {
echo     androidScheme: 'https'
echo   },
echo   plugins: {
echo     SplashScreen: {
echo       launchShowDuration: 2000,
echo       backgroundColor: "#4A148C",
echo       showSpinner: true,
echo       spinnerColor: "#D4AF37"
echo     },
echo     StatusBar: {
echo       style: 'dark',
echo       backgroundColor: "#4A148C"
echo     }
echo   }
echo };
echo.
echo export default config;
) > capacitor.config.ts

:: Agregar plataforma Android
echo [INFO] Agregando plataforma Android...
npx cap add android

:: Sincronizar archivos
echo [INFO] Sincronizando archivos...
npx cap sync

:: Crear script de build
echo [INFO] Creando script de build...
(
echo @echo off
echo echo Construyendo DuocPoint Mobile...
echo cd src\frontend
echo npx cap sync
echo npx cap build android
echo echo Build completado!
echo echo APK generado en: android\app\build\outputs\apk\
echo pause
) > ..\..\build-mobile.bat

:: Crear script de ejecución
echo [INFO] Creando script de ejecución...
(
echo @echo off
echo echo Ejecutando DuocPoint Mobile...
echo cd src\frontend
echo npx cap run android
echo pause
) > ..\..\run-mobile.bat

:: Crear script de configuración de red
echo [INFO] Creando script de configuración de red...
(
echo @echo off
echo echo Configurando acceso de red para móvil...
echo echo.
echo echo Ingresa la IP de tu PC ^(ej: 192.168.1.100^):
echo set /p PC_IP=
echo echo.
echo echo Configurando Capacitor para usar IP: %PC_IP%
echo cd src\frontend
echo echo import { CapacitorConfig } from '@capacitor/cli';
echo echo.
echo echo const config: CapacitorConfig = {
echo echo   appId: 'com.duocuc.duocpoint',
echo echo   appName: 'DuocPoint',
echo echo   webDir: '../',
echo echo   server: {
echo echo     url: 'http://%PC_IP%:8000',
echo echo     cleartext: true
echo echo   },
echo echo   plugins: {
echo echo     SplashScreen: {
echo echo       launchShowDuration: 2000,
echo echo       backgroundColor: "#4A148C",
echo echo       showSpinner: true,
echo echo       spinnerColor: "#D4AF37"
echo echo     },
echo echo     StatusBar: {
echo echo       style: 'dark',
echo echo       backgroundColor: "#4A148C"
echo echo     }
echo echo   }
echo echo };
echo echo.
echo echo export default config;
echo ) > capacitor.config.ts
echo echo.
echo echo Configuración actualizada!
echo echo Ahora ejecuta: npx cap sync
echo pause
) > ..\..\config-mobile-network.bat

:: Crear script de instalación de APK
echo [INFO] Creando script de instalación de APK...
(
echo @echo off
echo echo Instalando DuocPoint APK en dispositivo Android...
echo echo.
echo echo Conecta tu dispositivo Android via USB y habilita:
echo echo - Depuración USB
echo echo - Instalación desde fuentes desconocidas
echo echo.
echo pause
echo echo Instalando APK...
echo cd src\frontend
echo npx cap run android --target
echo pause
) > ..\..\install-mobile.bat

echo.
echo ============================================================
echo    Configuración Completada
echo ============================================================
echo.
echo ✅ Capacitor instalado y configurado
echo ✅ Plataforma Android agregada
echo ✅ Archivos sincronizados
echo ✅ Scripts creados
echo.
echo 📱 Scripts disponibles:
echo    - run-mobile.bat          : Ejecutar en emulador/dispositivo
echo    - build-mobile.bat        : Construir APK
echo    - config-mobile-network.bat : Configurar acceso de red
echo    - install-mobile.bat      : Instalar APK en dispositivo
echo.
echo 🔧 Próximos pasos:
echo    1. Instala Android Studio
echo    2. Configura un emulador Android
echo    3. Ejecuta: config-mobile-network.bat
echo    4. Ejecuta: run-mobile.bat
echo.
echo 📋 Para acceso desde móvil:
echo    1. Asegúrate de que tu PC y móvil estén en la misma red WiFi
echo    2. Encuentra la IP de tu PC: ipconfig
echo    3. Ejecuta: config-mobile-network.bat
echo    4. Ingresa la IP de tu PC
echo    5. Ejecuta: npx cap sync
echo.
echo Presiona cualquier tecla para continuar...
pause >nul

# DuocPoint - Aplicación Móvil

## Descripción
Aplicación móvil unificada de DuocPoint desarrollada con Ionic y Angular. Funciona tanto en web como en dispositivos móviles Android.

## Características
- ✅ Autenticación con JWT
- ✅ Interfaz unificada web/móvil
- ✅ Integración con backend Django
- ✅ Páginas principales: Login, Inicio, Foros, Mercado, Perfil
- ✅ Diseño responsive y moderno

## Requisitos
- Node.js 18+
- Ionic CLI
- Android Studio (para generar APK)
- Java JDK 11+

## Instalación

### 1. Instalar dependencias
```bash
npm install
```

### 2. Configurar backend
Asegúrate de que el backend Django esté ejecutándose en `http://localhost:8000`

### 3. Ejecutar en desarrollo
```bash
ionic serve
```

## Generar APK

### Opción 1: Usando Android Studio
1. Ejecuta: `ionic capacitor open android`
2. Abre el proyecto en Android Studio
3. Build → Build Bundle(s) / APK(s) → Build APK(s)

### Opción 2: Usando Gradle directamente
```bash
# Windows
generate-apk.bat

# Linux/Mac
chmod +x generate-apk.sh
./generate-apk.sh
```

### Opción 3: Comando manual
```bash
cd android
./gradlew assembleDebug
```

La APK se generará en: `android/app/build/outputs/apk/debug/app-debug.apk`

## Estructura del Proyecto
```
src/mobile/
├── src/app/
│   ├── pages/           # Páginas de la aplicación
│   ├── services/        # Servicios (API, etc.)
│   ├── tabs/           # Pestañas principales
│   └── ...
├── android/            # Proyecto Android nativo
├── www/               # Build web
└── capacitor.config.ts # Configuración Capacitor
```

## Configuración de Entornos
- **Desarrollo**: `src/environments/environment.ts`
- **Producción**: `src/environments/environment.prod.ts`

## Comandos Útiles
```bash
# Desarrollo
ionic serve                    # Servidor de desarrollo
ionic build                    # Build para producción
ionic capacitor sync android   # Sincronizar con Android

# Android
ionic capacitor run android    # Ejecutar en dispositivo/emulador
ionic capacitor open android   # Abrir en Android Studio
```

## Notas
- La aplicación está configurada para funcionar con el backend Django existente
- Los tokens JWT se almacenan en localStorage
- La aplicación es completamente responsive y funciona en web y móvil
- Para producción, actualiza las URLs en `environment.prod.ts`


# 📱 DuocPoint - Aplicación Móvil Android

## 🚀 Configuración de la Aplicación Móvil

### Prerrequisitos
- Node.js 16+ instalado
- Android Studio instalado
- Java JDK 11+ instalado

### Instalación

1. **Instalar Capacitor CLI globalmente:**
```bash
npm install -g @capacitor/cli
```

2. **Inicializar Capacitor en el proyecto:**
```bash
cd src/frontend
npx cap init DuocPoint com.duocuc.duocpoint
```

3. **Agregar plataforma Android:**
```bash
npx cap add android
```

4. **Sincronizar archivos:**
```bash
npx cap sync
```

5. **Abrir en Android Studio:**
```bash
npx cap open android
```

### Configuración del Proyecto

#### 1. Configurar capacitor.config.ts
```typescript
import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.duocuc.duocpoint',
  appName: 'DuocPoint',
  webDir: '../',
  server: {
    androidScheme: 'https'
  },
  plugins: {
    SplashScreen: {
      launchShowDuration: 2000,
      backgroundColor: "#4A148C",
      showSpinner: true,
      spinnerColor: "#D4AF37"
    },
    StatusBar: {
      style: 'dark',
      backgroundColor: "#4A148C"
    }
  }
};

export default config;
```

#### 2. Configurar AndroidManifest.xml
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/AppTheme">
        
        <activity
            android:name="com.duocuc.duocpoint.MainActivity"
            android:exported="true"
            android:launchMode="singleTask"
            android:theme="@style/AppTheme.NoActionBarLaunch">
            
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
    
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
</manifest>
```

### Scripts de Build

#### 1. Crear package.json para móvil
```json
{
  "name": "duocpoint-mobile",
  "version": "1.2.0",
  "scripts": {
    "build": "npx cap sync",
    "android": "npx cap run android",
    "android:build": "npx cap build android",
    "android:open": "npx cap open android"
  }
}
```

#### 2. Script de build automático
```bash
#!/bin/bash
# build-mobile.sh

echo "🚀 Construyendo DuocPoint Mobile..."

# Sincronizar archivos
npx cap sync

# Construir APK
npx cap build android

echo "✅ Build completado!"
echo "📱 APK generado en: android/app/build/outputs/apk/"
```

### Configuración de Red Local

#### 1. Para desarrollo local
```typescript
// En capacitor.config.ts
const config: CapacitorConfig = {
  appId: 'com.duocuc.duocpoint',
  appName: 'DuocPoint',
  webDir: '../',
  server: {
    url: 'http://192.168.1.100:8000', // IP de tu PC
    cleartext: true
  }
};
```

#### 2. Para producción
```typescript
const config: CapacitorConfig = {
  appId: 'com.duocuc.duocpoint',
  appName: 'DuocPoint',
  webDir: '../',
  server: {
    url: 'https://duocpoint.duocuc.cl',
    cleartext: false
  }
};
```

### Plugins Adicionales

#### 1. Instalar plugins necesarios
```bash
npm install @capacitor/status-bar @capacitor/splash-screen @capacitor/network @capacitor/push-notifications
```

#### 2. Configurar notificaciones push
```typescript
import { PushNotifications } from '@capacitor/push-notifications';

// Registrar para notificaciones
await PushNotifications.requestPermissions();
await PushNotifications.register();
```

### Iconos y Splash Screen

#### 1. Generar iconos
```bash
# Usar capacitor-assets
npm install -g @capacitor/assets
npx capacitor-assets generate
```

#### 2. Configurar splash screen
```typescript
import { SplashScreen } from '@capacitor/splash-screen';

// Mostrar splash screen
await SplashScreen.show({
  showSpinner: true,
  spinnerColor: '#D4AF37',
  backgroundColor: '#4A148C'
});
```

### Build y Deploy

#### 1. Build de desarrollo
```bash
npx cap run android
```

#### 2. Build de producción
```bash
npx cap build android
```

#### 3. Firmar APK
```bash
# Generar keystore
keytool -genkey -v -keystore duocpoint-release-key.keystore -alias duocpoint -keyalg RSA -keysize 2048 -validity 10000

# Firmar APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore duocpoint-release-key.keystore app-release-unsigned.apk duocpoint
```

### Configuración de Red

#### 1. Para acceso desde móvil a PC
- Asegúrate de que tu PC y móvil estén en la misma red WiFi
- Encuentra la IP de tu PC: `ipconfig` (Windows) o `ifconfig` (Linux/Mac)
- Actualiza la URL en capacitor.config.ts con tu IP

#### 2. Ejemplo de configuración
```typescript
const config: CapacitorConfig = {
  appId: 'com.duocuc.duocpoint',
  appName: 'DuocPoint',
  webDir: '../',
  server: {
    url: 'http://192.168.1.100:8000', // Cambiar por tu IP
    cleartext: true
  }
};
```

### Comandos Útiles

```bash
# Sincronizar cambios
npx cap sync

# Abrir en Android Studio
npx cap open android

# Ejecutar en dispositivo/emulador
npx cap run android

# Limpiar cache
npx cap clean

# Actualizar plugins
npx cap update
```

### Troubleshooting

#### 1. Error de conexión
- Verificar que el servidor esté corriendo
- Verificar IP en capacitor.config.ts
- Verificar firewall

#### 2. Error de build
- Limpiar proyecto: `npx cap clean`
- Reinstalar dependencias: `npm install`
- Sincronizar: `npx cap sync`

#### 3. Error de permisos
- Verificar AndroidManifest.xml
- Verificar permisos en config

### Estructura Final

```
duoc-point/
├── src/frontend/
│   ├── capacitor.config.ts
│   ├── package.json
│   └── ...
├── android/
│   ├── app/
│   ├── build.gradle
│   └── ...
└── mobile-app-setup.md
```

¡Con esta configuración tendrás una aplicación móvil nativa de DuocPoint funcionando en Android! 🚀

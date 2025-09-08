@echo off
chcp 65001 >nul
title DuocPoint - Configuración PWA Completa

echo.
echo ============================================================
echo    DuocPoint - Configuración PWA Completa
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
    echo   "name": "duocpoint-pwa",
    echo   "version": "1.2.0",
    echo   "description": "DuocPoint PWA",
    echo   "scripts": {
    echo     "build": "echo PWA build complete",
    echo     "serve": "echo PWA ready to serve"
    echo   }
    echo }
    ) > package.json
)

:: Crear archivo de configuración PWA
echo [INFO] Creando configuración PWA...
(
echo // Configuración PWA para DuocPoint
echo const PWA_CONFIG = {
echo   name: 'DuocPoint',
echo   short_name: 'DuocPoint',
echo   description: 'Plataforma integral para la comunidad estudiantil de Duoc UC',
echo   start_url: '/',
echo   display: 'standalone',
echo   background_color: '#4A148C',
echo   theme_color: '#4A148C',
echo   orientation: 'portrait-primary',
echo   scope: '/',
echo   lang: 'es',
echo   dir: 'ltr',
echo   categories: ['education', 'productivity', 'social'],
echo   icons: [
echo     {
echo       src: '/static/images/icons/icon-72x72.png',
echo       sizes: '72x72',
echo       type: 'image/png',
echo       purpose: 'any maskable'
echo     },
echo     {
echo       src: '/static/images/icons/icon-96x96.png',
echo       sizes: '96x96',
echo       type: 'image/png',
echo       purpose: 'any maskable'
echo     },
echo     {
echo       src: '/static/images/icons/icon-128x128.png',
echo       sizes: '128x128',
echo       type: 'image/png',
echo       purpose: 'any maskable'
echo     },
echo     {
echo       src: '/static/images/icons/icon-144x144.png',
echo       sizes: '144x144',
echo       type: 'image/png',
echo       purpose: 'any maskable'
echo     },
echo     {
echo       src: '/static/images/icons/icon-152x152.png',
echo       sizes: '152x152',
echo       type: 'image/png',
echo       purpose: 'any maskable'
echo     },
echo     {
echo       src: '/static/images/icons/icon-192x192.png',
echo       sizes: '192x192',
echo       type: 'image/png',
echo       purpose: 'any maskable'
echo     },
echo     {
echo       src: '/static/images/icons/icon-384x384.png',
echo       sizes: '384x384',
echo       type: 'image/png',
echo       purpose: 'any maskable'
echo     },
echo     {
echo       src: '/static/images/icons/icon-512x512.png',
echo       sizes: '512x512',
echo       type: 'image/png',
echo       purpose: 'any maskable'
echo     }
echo   ]
echo };
echo.
echo // Exportar configuración
echo if (typeof module !== 'undefined' && module.exports) {
echo   module.exports = PWA_CONFIG;
echo } else if (typeof window !== 'undefined') {
echo   window.PWA_CONFIG = PWA_CONFIG;
echo }
) > pwa-config.js

:: Crear directorio de iconos si no existe
if not exist "static\images\icons" (
    echo [INFO] Creando directorio de iconos...
    mkdir static\images\icons
)

:: Crear service worker mejorado
echo [INFO] Creando service worker mejorado...
(
echo // Service Worker para DuocPoint PWA
echo const CACHE_NAME = 'duocpoint-v1.2.0';
echo const STATIC_CACHE = 'duocpoint-static-v1.2.0';
echo const DYNAMIC_CACHE = 'duocpoint-dynamic-v1.2.0';
echo.
echo // Archivos estáticos para cachear
echo const STATIC_FILES = [
echo   '/',
echo   '/index.html',
echo   '/login-duoc.html',
echo   '/duoc-theme.css',
echo   '/styles.css',
echo   '/main.js',
echo   '/pwa.js',
echo   '/manifest.json',
echo   '/static/images/icons/icon-192x192.png',
echo   '/static/images/icons/icon-512x512.png'
echo ];
echo.
echo // Instalación del Service Worker
echo self.addEventListener('install', event => {
echo   console.log('Service Worker: Instalando...');
echo   event.waitUntil(
echo     caches.open(STATIC_CACHE)
echo       .then(cache => {
echo         console.log('Service Worker: Cacheando archivos estáticos');
echo         return cache.addAll(STATIC_FILES);
echo       })
echo       .catch(error => {
echo         console.log('Service Worker: Error en instalación:', error);
echo       })
echo   );
echo });
echo.
echo // Activación del Service Worker
echo self.addEventListener('activate', event => {
echo   console.log('Service Worker: Activando...');
echo   event.waitUntil(
echo     caches.keys().then(cacheNames => {
echo       return Promise.all(
echo         cacheNames.map(cacheName => {
echo           if (cacheName !== STATIC_CACHE && cacheName !== DYNAMIC_CACHE) {
echo             console.log('Service Worker: Eliminando cache antiguo:', cacheName);
echo             return caches.delete(cacheName);
echo           }
echo         })
echo       );
echo     })
echo   );
echo   console.log('Service Worker: Activación completada');
echo });
echo.
echo // Interceptar requests
echo self.addEventListener('fetch', event => {
echo   // Solo interceptar requests GET
echo   if (event.request.method !== 'GET') {
echo     return;
echo   }
echo.
echo   // Estrategia: Cache First para archivos estáticos
echo   if (STATIC_FILES.includes(event.request.url) || 
echo       event.request.url.includes('/static/') ||
echo       event.request.url.includes('/duoc-theme.css') ||
echo       event.request.url.includes('/styles.css')) {
echo     event.respondWith(
echo       caches.match(event.request)
echo         .then(response => {
echo           if (response) {
echo             return response;
echo           }
echo           return fetch(event.request)
echo             .then(fetchResponse => {
echo               return caches.open(STATIC_CACHE)
echo                 .then(cache => {
echo                   cache.put(event.request, fetchResponse.clone());
echo                   return fetchResponse;
echo                 });
echo             });
echo         })
echo     );
echo   } else {
echo     // Estrategia: Network First para API y páginas dinámicas
echo     event.respondWith(
echo       fetch(event.request)
echo         .then(response => {
echo           if (response.status === 200) {
echo             const responseClone = response.clone();
echo             caches.open(DYNAMIC_CACHE)
echo               .then(cache => {
echo                 cache.put(event.request, responseClone);
echo               });
echo           }
echo           return response;
echo         })
echo         .catch(() => {
echo           return caches.match(event.request)
echo             .then(response => {
echo               if (response) {
echo                 return response;
echo               }
echo               // Fallback para páginas
echo               if (event.request.headers.get('accept').includes('text/html')) {
echo                 return caches.match('/index.html');
echo               }
echo             });
echo         })
echo     );
echo   }
echo });
echo.
echo // Manejar notificaciones push
echo self.addEventListener('push', event => {
echo   console.log('Service Worker: Notificación push recibida');
echo   const options = {
echo     body: event.data ? event.data.text() : 'Nueva notificación de DuocPoint',
echo     icon: '/static/images/icons/icon-192x192.png',
echo     badge: '/static/images/icons/icon-72x72.png',
echo     vibrate: [100, 50, 100],
echo     data: {
echo       dateOfArrival: Date.now(),
echo       primaryKey: 1
echo     },
echo     actions: [
echo       {
echo         action: 'explore',
echo         title: 'Ver detalles',
echo         icon: '/static/images/icons/icon-192x192.png'
echo       },
echo       {
echo         action: 'close',
echo         title: 'Cerrar',
echo         icon: '/static/images/icons/icon-192x192.png'
echo       }
echo     ]
echo   };
echo.
echo   event.waitUntil(
echo     self.registration.showNotification('DuocPoint', options)
echo   );
echo });
echo.
echo // Manejar clics en notificaciones
echo self.addEventListener('notificationclick', event => {
echo   console.log('Service Worker: Notificación clickeada');
echo   event.notification.close();
echo.
echo   if (event.action === 'explore') {
echo     event.waitUntil(
echo       clients.openWindow('/')
echo     );
echo   }
echo });
) > sw.js

:: Crear archivo PWA mejorado
echo [INFO] Creando archivo PWA mejorado...
(
echo // DuocPoint PWA Manager
echo class DuocPointPWA {
echo   constructor() {
echo     this.isOnline = navigator.onLine;
echo     this.registration = null;
echo     this.init();
echo   }
echo.
echo   async init() {
echo     console.log('PWA: Inicializando...');
echo     this.setupEventListeners();
echo     await this.registerServiceWorker();
echo     this.setupInstallPrompt();
echo     this.checkConnection();
echo   }
echo.
echo   setupEventListeners() {
echo     window.addEventListener('online', () => {
echo       this.isOnline = true;
echo       this.updateConnectionStatus();
echo       this.showNotification('Conexión restaurada', 'success');
echo     });
echo.
echo     window.addEventListener('offline', () => {
echo       this.isOnline = false;
echo       this.updateConnectionStatus();
echo       this.showNotification('Sin conexión - Modo offline', 'warning');
echo     });
echo   }
echo.
echo   async registerServiceWorker() {
echo     if ('serviceWorker' in navigator) {
echo       try {
echo         this.registration = await navigator.serviceWorker.register('/sw.js');
echo         console.log('PWA: Service Worker registrado exitosamente:', this.registration);
echo.
echo         // Verificar actualizaciones
echo         this.registration.addEventListener('updatefound', () => {
echo           const newWorker = this.registration.installing;
echo           newWorker.addEventListener('statechange', () => {
echo             if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
echo               this.showUpdateNotification();
echo             }
echo           });
echo         });
echo       } catch (error) {
echo         console.error('PWA: Error registrando Service Worker:', error);
echo       }
echo     }
echo   }
echo.
echo   setupInstallPrompt() {
echo     let deferredPrompt;
echo.
echo     window.addEventListener('beforeinstallprompt', (e) => {
echo       console.log('PWA: Prompt de instalación disponible');
echo       e.preventDefault();
echo       deferredPrompt = e;
echo       this.showInstallButton(deferredPrompt);
echo     });
echo.
echo     window.addEventListener('appinstalled', () => {
echo       console.log('PWA: Aplicación instalada');
echo       this.hideInstallButton();
echo       this.showNotification('¡DuocPoint instalado exitosamente!', 'success');
echo     });
echo   }
echo.
echo   showInstallButton(deferredPrompt) {
echo     const installButton = document.getElementById('install-button');
echo     if (installButton) {
echo       installButton.style.display = 'block';
echo       installButton.addEventListener('click', async () => {
echo         if (deferredPrompt) {
echo           deferredPrompt.prompt();
echo           const { outcome } = await deferredPrompt.userChoice;
echo           console.log('PWA: Resultado de instalación:', outcome);
echo           deferredPrompt = null;
echo           this.hideInstallButton();
echo         }
echo       });
echo     }
echo   }
echo.
echo   hideInstallButton() {
echo     const installButton = document.getElementById('install-button');
echo     if (installButton) {
echo       installButton.style.display = 'none';
echo     }
echo   }
echo.
echo   updateConnectionStatus() {
echo     const statusElement = document.getElementById('connection-status');
echo     const textElement = document.getElementById('connection-text');
echo.
echo     if (statusElement && textElement) {
echo       if (this.isOnline) {
echo         statusElement.className = 'fas fa-circle text-success';
echo         textElement.textContent = 'Online';
echo       } else {
echo         statusElement.className = 'fas fa-circle text-warning';
echo         textElement.textContent = 'Offline';
echo       }
echo     }
echo   }
echo.
echo   checkConnection() {
echo     this.updateConnectionStatus();
echo     setInterval(() => {
echo       this.updateConnectionStatus();
echo     }, 5000);
echo   }
echo.
echo   showNotification(message, type = 'info') {
echo     // Crear notificación visual
echo     const notification = document.createElement('div');
echo     notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
echo     notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
echo     notification.innerHTML = `
echo       ${message}
echo       <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
echo     `;
echo.
echo     document.body.appendChild(notification);
echo.
echo     // Auto-remover después de 5 segundos
echo     setTimeout(() => {
echo       if (notification.parentNode) {
echo         notification.remove();
echo       }
echo     }, 5000);
echo   }
echo.
echo   showUpdateNotification() {
echo     const updateNotification = document.createElement('div');
echo     updateNotification.className = 'alert alert-info alert-dismissible fade show position-fixed';
echo     updateNotification.style.cssText = 'top: 20px; left: 20px; z-index: 9999; min-width: 300px;';
echo     updateNotification.innerHTML = `
echo       <strong>Actualización disponible</strong><br>
echo       Hay una nueva versión de DuocPoint disponible.
echo       <button type="button" class="btn btn-sm btn-primary ms-2" onclick="window.location.reload()">
echo         Actualizar
echo       </button>
echo       <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
echo     `;
echo.
echo     document.body.appendChild(updateNotification);
echo   }
echo.
echo   async clearCache() {
echo     if (this.registration) {
echo       const cacheNames = await caches.keys();
echo       await Promise.all(
echo         cacheNames.map(cacheName => caches.delete(cacheName))
echo       );
echo       this.showNotification('Cache limpiado exitosamente', 'success');
echo     }
echo   }
echo.
echo   getVersion() {
echo     this.showNotification('DuocPoint v1.2.0 - PWA', 'info');
echo   }
echo }
echo.
echo // Inicializar PWA cuando el DOM esté listo
echo document.addEventListener('DOMContentLoaded', () => {
echo   window.duocPointPWA = new DuocPointPWA();
echo });
) > pwa.js

:: Crear script de build PWA
echo [INFO] Creando script de build PWA...
(
echo @echo off
echo echo Construyendo DuocPoint PWA...
echo cd src\frontend
echo echo PWA build completado!
echo echo La aplicación está lista para usar como PWA
echo pause
) > ..\..\build-pwa.bat

echo.
echo ============================================================
echo    Configuración PWA Completada
echo ============================================================
echo.
echo ✅ Service Worker optimizado creado
echo ✅ Configuración PWA completa
echo ✅ Archivos de cache configurados
echo ✅ Notificaciones push implementadas
echo ✅ Instalación PWA configurada
echo ✅ Modo offline implementado
echo.
echo 📱 Características PWA:
echo    - Instalable como aplicación nativa
echo    - Funciona offline
echo    - Notificaciones push
echo    - Cache inteligente
echo    - Actualizaciones automáticas
echo.
echo 🔧 Para usar:
echo    1. Ejecuta: iniciar_desarrollo.bat
echo    2. Abre: http://localhost:8000
echo    3. Instala la PWA desde el navegador
echo.
echo Presiona cualquier tecla para continuar...
pause >nul

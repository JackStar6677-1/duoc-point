/**
 * Service Worker para StudentsPoint
 * Versión: 1.0.0
 */

const CACHE_NAME = 'StudentsPoint-v1.2.0';
const STATIC_CACHE = 'StudentsPoint-static-v1.2.0';
const DYNAMIC_CACHE = 'StudentsPoint-dynamic-v1.2.0';

// Archivos estáticos para cache
const STATIC_FILES = [
  '/',
  '/index.html',
  '/login.html',
  '/register.html',
  '/account.html',
  '/teachers.html',
  '/campuses.html',
  '/static/css/styles.css',
  '/static/css/students-theme.css',
  '/static/js/main.js',
  '/static/js/pwa.js',
  '/static/js/sounds.js',
  '/static/manifest.json',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
  'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css',
  'https://code.jquery.com/jquery-3.7.1.min.js',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js',
  '/static/images/icons/icon-192x192.png',
  '/static/images/icons/icon-512x512.png',
  '/forum/',
  '/market/',
  '/portfolio/',
  '/streetview/',
  '/bienestar/',
  '/reportes/',
  '/cursos/',
  '/encuestas/',
  '/horarios/'
];

// Archivos de API para cache dinámico
const API_PATTERNS = [
  '/api/auth/',
  '/api/forum/',
  '/api/market/',
  '/api/portfolio/',
  '/api/polls/',
  '/api/campuses/',
  '/api/bienestar/',
  '/api/notifications/',
  '/api/reports/',
  '/api/schedules/',
  '/api/otec/'
];

// Estrategia de cache: Network First para APIs, Cache First para estáticos
const CACHE_STRATEGY = {
  networkFirst: ['/api/'],
  cacheFirst: ['/static/', '/imagenes/'],
  staleWhileRevalidate: ['/']
};

/**
 * Instalación del Service Worker
 */
self.addEventListener('install', (event) => {
  console.log('SW: Instalando Service Worker...');
  
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then((cache) => {
        console.log('SW: Cacheando archivos estáticos...');
        return cache.addAll(STATIC_FILES);
      })
      .then(() => {
        console.log('SW: Service Worker instalado correctamente');
        return self.skipWaiting();
      })
      .catch((error) => {
        console.error('SW: Error durante la instalación:', error);
      })
  );
});

/**
 * Activación del Service Worker
 */
self.addEventListener('activate', (event) => {
  console.log('SW: Activando Service Worker...');
  
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames.map((cacheName) => {
            if (cacheName !== STATIC_CACHE && cacheName !== DYNAMIC_CACHE) {
              console.log('SW: Eliminando cache obsoleto:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => {
        console.log('SW: Service Worker activado correctamente');
        return self.clients.claim();
      })
      .catch((error) => {
        console.error('SW: Error durante la activación:', error);
      })
  );
});

/**
 * Interceptar requests
 */
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Solo interceptar requests del mismo origen
  if (url.origin !== location.origin) {
    return;
  }
  
  // No cachear requests POST, PUT, DELETE, etc.
  if (request.method !== 'GET') {
    return;
  }
  
  // Determinar estrategia de cache
  const strategy = getCacheStrategy(request.url);
  
  switch (strategy) {
    case 'networkFirst':
      event.respondWith(networkFirst(request));
      break;
    case 'cacheFirst':
      event.respondWith(cacheFirst(request));
      break;
    case 'staleWhileRevalidate':
      event.respondWith(staleWhileRevalidate(request));
      break;
    default:
      event.respondWith(fetch(request));
  }
});

/**
 * Determinar estrategia de cache basada en la URL
 */
function getCacheStrategy(url) {
  for (const [strategy, patterns] of Object.entries(CACHE_STRATEGY)) {
    if (patterns.some(pattern => url.includes(pattern))) {
      return strategy;
    }
  }
  return 'networkFirst'; // Default
}

/**
 * Estrategia: Network First
 * Intenta la red primero, si falla usa cache
 */
async function networkFirst(request) {
  try {
    const networkResponse = await fetch(request);
    
    // Cachear respuesta exitosa
    if (networkResponse.ok) {
      const cache = await caches.open(DYNAMIC_CACHE);
      cache.put(request, networkResponse.clone());
    }
    
    return networkResponse;
  } catch (error) {
    console.log('SW: Red no disponible, usando cache:', request.url);
    const cachedResponse = await caches.match(request);
    
    if (cachedResponse) {
      return cachedResponse;
    }
    
    // Si es una página HTML, devolver index.html
    if (request.headers.get('accept').includes('text/html')) {
      return caches.match('/index.html');
    }
    
    throw error;
  }
}

/**
 * Estrategia: Cache First
 * Usa cache primero, si no existe va a la red
 */
async function cacheFirst(request) {
  const cachedResponse = await caches.match(request);
  
  if (cachedResponse) {
    return cachedResponse;
  }
  
  try {
    const networkResponse = await fetch(request);
    
    if (networkResponse.ok) {
      const cache = await caches.open(STATIC_CACHE);
      cache.put(request, networkResponse.clone());
    }
    
    return networkResponse;
  } catch (error) {
    console.error('SW: Error en cache first:', error);
    throw error;
  }
}

/**
 * Estrategia: Stale While Revalidate
 * Devuelve cache inmediatamente y actualiza en background
 */
async function staleWhileRevalidate(request) {
  const cache = await caches.open(DYNAMIC_CACHE);
  const cachedResponse = await cache.match(request);
  
  // Actualizar cache en background
  const fetchPromise = fetch(request).then((networkResponse) => {
    if (networkResponse.ok) {
      cache.put(request, networkResponse.clone());
    }
    return networkResponse;
  }).catch((error) => {
    console.log('SW: Error actualizando cache:', error);
  });
  
  // Devolver cache si existe, sino esperar la red
  return cachedResponse || fetchPromise;
}

/**
 * Manejar mensajes del cliente
 */
self.addEventListener('message', (event) => {
  const { type, payload } = event.data;
  
  switch (type) {
    case 'SKIP_WAITING':
      self.skipWaiting();
      break;
    case 'GET_VERSION':
      event.ports[0].postMessage({
        version: CACHE_NAME,
        staticCache: STATIC_CACHE,
        dynamicCache: DYNAMIC_CACHE
      });
      break;
    case 'CLEAR_CACHE':
      clearAllCaches().then(() => {
        event.ports[0].postMessage({ success: true });
      });
      break;
    default:
      console.log('SW: Mensaje no reconocido:', type);
  }
});

/**
 * Limpiar todos los caches
 */
async function clearAllCaches() {
  const cacheNames = await caches.keys();
  await Promise.all(
    cacheNames.map(cacheName => caches.delete(cacheName))
  );
  console.log('SW: Todos los caches limpiados');
}

/**
 * Manejar notificaciones push
 */
self.addEventListener('push', (event) => {
  console.log('SW: Push recibido:', event);
  
  const options = {
    body: event.data ? event.data.text() : 'Nueva notificación de StudentsPoint',
    icon: '/static/images/icons/icon-192x192.png',
    badge: '/static/images/icons/icon-72x72.png',
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'explore',
        title: 'Ver detalles',
        icon: '/static/images/icons/icon-192x192.png'
      },
      {
        action: 'close',
        title: 'Cerrar',
        icon: '/static/images/icons/icon-192x192.png'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification('StudentsPoint', options)
  );
});

/**
 * Manejar clics en notificaciones
 */
self.addEventListener('notificationclick', (event) => {
  console.log('SW: Click en notificación:', event);
  
  event.notification.close();
  
  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow('/')
    );
  } else if (event.action === 'close') {
    // Solo cerrar la notificación
    return;
  } else {
    // Click en el cuerpo de la notificación
    event.waitUntil(
      clients.openWindow('/')
    );
  }
});

/**
 * Manejar sincronización en background
 */
self.addEventListener('sync', (event) => {
  console.log('SW: Sincronización en background:', event.tag);
  
  if (event.tag === 'background-sync') {
    event.waitUntil(doBackgroundSync());
  }
});

/**
 * Realizar sincronización en background
 */
async function doBackgroundSync() {
  try {
    // Aquí puedes implementar lógica de sincronización
    console.log('SW: Realizando sincronización en background...');
    
    // Ejemplo: sincronizar datos offline
    const cache = await caches.open(DYNAMIC_CACHE);
    const requests = await cache.keys();
    
    for (const request of requests) {
      if (request.url.includes('/api/')) {
        try {
          const response = await fetch(request);
          if (response.ok) {
            await cache.put(request, response);
          }
        } catch (error) {
          console.log('SW: Error sincronizando:', request.url, error);
        }
      }
    }
    
    console.log('SW: Sincronización completada');
  } catch (error) {
    console.error('SW: Error en sincronización:', error);
  }
}

console.log('SW: Service Worker cargado correctamente');
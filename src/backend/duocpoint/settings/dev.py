from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*",
    "192.168.100.2",
    "192.168.100.6",
]

# Deshabilitar CSRF para APIs
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
    "http://192.168.100.2:8000",
    "http://192.168.100.1:8000",
    "http://192.168.1.1:8000",
    "http://192.168.0.1:8000",
    "http://192.168.100.6:8000",
]

# Deshabilitar CSRF para APIs REST
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = False
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
    "http://192.168.100.2:8000",
    "http://192.168.100.1:8000",
    "http://192.168.1.1:8000",
    "http://192.168.0.1:8000",
    "http://192.168.100.6:8000",
]

# Permitir CORS para desarrollo
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Configuración para PWA en red local - IPs dinámicas
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    # IPs comunes de red local (se agregan automáticamente)
    "192.168.1.*",
    "192.168.0.*", 
    "192.168.100.*",
    "10.0.0.*",
    "172.16.*",
    "172.17.*",
    "172.18.*",
    "172.19.*",
    "172.20.*",
    "172.21.*",
    "172.22.*",
    "172.23.*",
    "172.24.*",
    "172.25.*",
    "172.26.*",
    "172.27.*",
    "172.28.*",
    "172.29.*",
    "172.30.*",
    "172.31.*",
    "*"  # Permitir cualquier host en desarrollo
]
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*",
    "192.168.100.2",
    "192.168.100.6",
    "192.168.100.59",
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
    "http://192.168.100.59:8000",
]

# Deshabilitar CSRF para APIs REST
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = False
CSRF_COOKIE_SAMESITE = 'Lax'

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

# (única definición) CSRF_TRUSTED_ORIGINS definida arriba

# (única definición) ALLOWED_HOSTS definida arriba

# Configuración de archivos estáticos para desarrollo
STATICFILES_DIRS = [
    BASE_DIR.parent / "frontend/static",
]

# Configuración para servir archivos estáticos en desarrollo
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
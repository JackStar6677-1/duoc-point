"""
Configuración de testing para StudentsPoint
"""

from datetime import timedelta
from .base import *

# Configuración específica para testing
DEBUG = False
TEMPLATE_DEBUG = False

# Base de datos en memoria para tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Cache en memoria para tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Configuración de email para tests
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Configuración de archivos estáticos para tests
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Configuración de logging para tests
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    },
}

# Configuración de JWT para tests
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'test-secret-key',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Configuración de Celery para tests
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Configuración de Redis para tests
REDIS_URL = 'redis://localhost:6379/1'

# Configuración de archivos media para tests
MEDIA_ROOT = '/tmp/studentspoint_test_media/'

# Configuración de seguridad para tests
SECRET_KEY = 'test-secret-key-for-testing-only'
ALLOWED_HOSTS = ['testserver']

# Configuración de CORS para tests
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Configuración de PWA para tests
PWA_APP_NAME = 'StudentsPoint Test'
PWA_APP_DESCRIPTION = 'StudentsPoint Test App'
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/images/icon-192x192.png',
        'sizes': '192x192'
    }
]

# Configuración de Google OAuth para tests (deshabilitado)
GOOGLE_OAUTH2_CLIENT_ID = None
GOOGLE_OAUTH2_CLIENT_SECRET = None

# Configuración de Google Maps para tests (deshabilitado)
GOOGLE_MAPS_API_KEY = None

# Configuración de Web Push para tests
VAPID_PUBLIC_KEY = 'test-public-key'
VAPID_PRIVATE_KEY = 'test-private-key'
VAPID_ADMIN_EMAIL = 'test@example.com'

# Configuración de OpenGraph para tests
OPENGRAPH_APP_ID = 'test-app-id'

# Configuración de Chart.js para tests
CHARTJS_CDN = 'https://cdn.jsdelivr.net/npm/chart.js'

# Configuración de Leaflet para tests
LEAFLET_CDN = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js'

# Configuración de Bootstrap para tests
BOOTSTRAP_CDN = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'

# Configuración de Font Awesome para tests
FONTAWESOME_CDN = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'

# Configuración de jQuery para tests
JQUERY_CDN = 'https://code.jquery.com/jquery-3.7.1.min.js'

# Configuración de Popper.js para tests
POPPER_CDN = 'https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js'

# Configuración de Bootstrap JS para tests
BOOTSTRAP_JS_CDN = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js'

# Configuración de WeasyPrint para tests (deshabilitado en Windows)
WEASYPRINT_ENABLED = False

# Configuración de PyPDF2 para tests
PYPDF2_ENABLED = True

# Configuración de Pillow para tests
PILLOW_ENABLED = True

# Configuración de Celery Beat para tests
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Configuración de Django Debug Toolbar para tests (deshabilitado)
DEBUG_TOOLBAR_ENABLED = False

# Configuración de Django Extensions para tests
EXTENSIONS_ENABLED = False

# Configuración de Django CORS Headers para tests
CORS_HEADERS_ENABLED = True

# Configuración de Django REST Framework para tests
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
    ],
}

# Configuración de Django Filter para tests
FILTERS_ENABLED = True

# Configuración de Django CORS Headers para tests
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False

# Configuración de Django REST Framework Simple JWT para tests
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'test-secret-key',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Configuración de Django Celery Beat para tests
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Configuración de Django Celery Results para tests
CELERY_RESULT_BACKEND = 'django-db'

# Configuración de Django Celery Beat para tests
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Configuración de Django Celery Results para tests
CELERY_RESULT_BACKEND = 'django-db'

# Configuración de Django Celery Beat para tests
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Configuración de Django Celery Results para tests
CELERY_RESULT_BACKEND = 'django-db'

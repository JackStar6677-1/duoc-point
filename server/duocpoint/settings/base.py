from pathlib import Path
import os

# base.py está en: server/duocpoint/settings/base.py
# Queremos que BASE_DIR sea: server/
BASE_DIR = Path(__file__).resolve().parents[2]

# ---- Seguridad / debug ----
SECRET_KEY = os.getenv("SECRET_KEY", "dev-insecure")
DEBUG = os.getenv("DEBUG", "1") == "1"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# ---- Apps ----
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 3rd party
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    "rest_framework_simplejwt",

    # Local apps (ajusta nombres si cambiaste rutas)
    "duocpoint.apps.accounts",
    "duocpoint.apps.campuses",
    "duocpoint.apps.forum",
    "duocpoint.apps.health",
    "duocpoint.apps.market",
    "duocpoint.apps.notifications",
    "duocpoint.apps.otec",
    "duocpoint.apps.polls",
    "duocpoint.apps.portfolio",
    "duocpoint.apps.reports",
    "duocpoint.apps.schedules",
    "duocpoint.apps.wellbeing",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "duocpoint.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # opcional, si usas templates globales
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "duocpoint.wsgi.application"
ASGI_APPLICATION = "duocpoint.asgi.application"  # por si luego usas Channels/WebSockets

# ---- Base de datos ----
# En dev parte con SQLite. Para Postgres, cambia variables por ENV.
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", ""),
    }
}

# ---- Idioma / zona horaria ----
LANGUAGE_CODE = "es-cl"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_TZ = True

# ---- Archivos estáticos y media ----
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
if (BASE_DIR / "static").exists():
    STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"

# ---- DRF ----
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.UserRateThrottle",
        "rest_framework.throttling.AnonRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"user": "1000/day", "anon": "100/day"},
}

if os.getenv("DEMO_MODE") == "1":
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = []
    REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = [
        "rest_framework.permissions.AllowAny"
    ]

SPECTACULAR_SETTINGS = {
    "TITLE": "Duoc-Point API",
    "DESCRIPTION": "Esquema de la API",
    "VERSION": "1.0.0",
}


# ---- CORS ----
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:3000").split(",")


# ---- Google OAuth (DESHABILITADO) ----
# GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID", "")


# ---- Google Maps/Street View (DESHABILITADO - USAMOS STREET VIEW PERSONALIZADO) ----
# GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")


# ---- Celery ----
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", CELERY_BROKER_URL)

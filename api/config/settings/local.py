from datetime import timedelta
from os import getenv, path

from dotenv import load_dotenv

from .base import *  # noqa
from .base import BASE_DIR  # noqa

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")
if path.isfile(local_env_file):
    load_dotenv(local_env_file)


DEBUG = True

# Site and Security Settings
SITE_NAME = getenv("SITE_NAME", "Django Real Estate")
SECRET_KEY = getenv("DJANGO_SECRET_KEY")


if not SECRET_KEY:
    raise ValueError("DJANGO_SECRET_KEY environment variable is not set!")

# Host configuration
ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "localhost,127.0.0.1,0.0.0.0").split(",")


ADMIN_URL = getenv("ADMIN_URL", "admin/")

# CSRF Settings - Added more origins for development
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
]
# Parse additional origins from environment if provided
additional_origins = getenv("CSRF_TRUSTED_ORIGINS_EXTRA", "")
if additional_origins:
    CSRF_TRUSTED_ORIGINS.extend(additional_origins.split(","))

# Email settings for development
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST", "localhost")  # Added default
EMAIL_PORT = getenv("EMAIL_PORT", "25")  # Added default, ensure it's string
# Convert EMAIL_PORT to int if needed
try:
    EMAIL_PORT = int(EMAIL_PORT)
except (ValueError, TypeError):
    EMAIL_PORT = 25

DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL", "admin@localhost")
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER", "")  # Added for email auth
EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD", "")  # Added for email auth
EMAIL_USE_TLS = getenv("EMAIL_USE_TLS", "False").lower() == "true"  # Added TLS option

# File upload settings
MAX_UPLOAD_SIZE = 1 * 1024 * 1024  # 1MB

# Security settings for development
LOCKOUT_DURATION = timedelta(minutes=1)
LOGIN_ATTEMPTS = 3
OPT_EXPIRATION = timedelta(minutes=1)

# Django Debug Toolbar (optional, for development)
# if DEBUG:
#     INSTALLED_APPS += ["debug_toolbar"]  # noqa
#     MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa
#     INTERNAL_IPS = ["127.0.0.1"]

# Database configuration - Override if using PostgreSQL in development
# Uncomment if you want to use PostgreSQL locally
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": getenv("DB_NAME", "real_estate_dev"),
#         "USER": getenv("DB_USER", "postgres"),
#         "PASSWORD": getenv("DB_PASSWORD", ""),
#         "HOST": getenv("DB_HOST", "localhost"),
#         "PORT": getenv("DB_PORT", "5432"),
#     }
# }

# Celery settings for development
CELERY_BROKER_URL = getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

# Logging configuration for development
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}

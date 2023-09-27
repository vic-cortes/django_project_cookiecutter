from .base import *
from .config import Config

DEBUG = True

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": Config.DB_NAME,
        "USER": Config.DB_USER,
        "PASSWORD": Config.DB_PASSWORD,
        "HOST": "localhost",
        "PORT": Config.DB_PORT,
    }
}

INSTALLED_APPS += []

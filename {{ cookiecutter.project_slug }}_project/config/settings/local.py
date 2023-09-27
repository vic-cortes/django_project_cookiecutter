from .base import *

DEBUG = True

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "{{ cookiecutter.project_slug }}_db",
        "HOST": "localhost",
    }
}

INSTALLED_APPS += []

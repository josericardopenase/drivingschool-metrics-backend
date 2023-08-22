from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0', 'hidden-basin-07379-f12c228b10fd.herokuapp.com', 'api.econext.es']
DEBUG = os.getenv('DJANGO_DEBUG', False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


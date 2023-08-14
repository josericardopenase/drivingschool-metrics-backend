# project/settings/__init__.py

import os

if os.getenv('DJANGO_ENV') == 'production':
    from .production import *
else:
    from .base import *

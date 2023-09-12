"""
DEV-settings
"""
import os.path
from .base_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]

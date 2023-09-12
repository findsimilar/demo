"""
PROD-settings
python manage.py runserver --settings=backend.prod_settings
"""
import os
from .base_settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PGDB'),
        'USER': os.getenv('PGUSER'),
        'PASSWORD': os.getenv('PGPASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://api.findsimilar.org', 'http://188.64.12.238:8000']
STATIC_ROOT = 'static'

CORS_ALLOWED_ORIGINS = [
    'http://demo.findsimilar.org',
    'http://188.64.12.238',
    'http://188.64.12.238:8000'
]

"""
PROD-settings
python manage.py runserver --settings=backend.prod_settings
"""
from .base_settings import *


DEBUG = False
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = []
STATIC_ROOT = 'static'

CORS_ALLOWED_ORIGINS = [
    'https://demo.findsimilar.org',
]

"""
PROD-settings
python manage.py runserver --settings=backend.prod_settings
"""
from .base_settings import *


DEBUG = False
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000', 'api.findsimilar.org']
STATIC_ROOT = 'static'

CORS_ALLOWED_ORIGINS = [
    'http://demo.findsimilar.org',
]

"""
DEV-settings
"""
from .base_settings import *

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]
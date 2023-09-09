"""
DEV-settings
"""
import os
from demo.base_settings import BASE_DIR


STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

"""
PROD-settings
python manage.py runserver --settings=backend.prod_settings
"""


DEBUG = False
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://api.findsimilar.org", "http://188.64.12.238:8000"]
STATIC_ROOT = "static"

CORS_ALLOWED_ORIGINS = [
    "http://demo.findsimilar.org",
    "http://188.64.12.238",
    "http://188.64.12.238:8000",
]

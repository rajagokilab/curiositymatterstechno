from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "your-secret-key"

DEBUG = True
ALLOWED_HOSTS = [
    "curiositytechmatters.se",
    "www.curiositytechmatters.se",
    ".onrender.com","*",
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agency',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==========================================
# EMAIL CONFIGURATION
# ==========================================

# 1. LOCAL DEVELOPMENT (Active right now)
# Prints emails to your terminal to bypass your computer's Antivirus
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DEFAULT_FROM_EMAIL = 'rajagokilavivek@gmail.com'

# ---------------------------------------------------------
# 2. RENDER / PRODUCTION SETTINGS 
# (When you deploy to Render, delete the "Local Development" 
# block above, and remove the # symbols from the block below)
# ---------------------------------------------------------
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False
# EMAIL_HOST_USER = os.environ.get('rajagokilavivek@gmail.com')
# EMAIL_HOST_PASSWORD = os.environ.get('mnvg hcly pcet hmje')
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ==========================================
# EMAIL CONFIGURATION (PRODUCTION)
# ==========================================
# import os

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'

# # Using Port 465 and SSL prevents STARTTLS timeouts on Render
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False

# # Pulling securely from Render's Environment Variables
# EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ==========================================
# EMAIL CONFIGURATION (PRODUCTION - RENDER)
# ==========================================
import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'

# CRITICAL FIX: Use Port 465 and SSL for Render deployments to avoid timeouts
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

# Fallback defaults for local testing, overridden by Render environment variables
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "rajagokilavivek@gmail.com")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "mnvg hcly pcet hmje")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
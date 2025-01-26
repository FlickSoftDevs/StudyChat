import os
import configparser
import cloudinary
import cloudinary_storage
import cloudinary.api
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')

# Secret key
SECRET_KEY = '!5rt_gri@0-_0+#*nyb6+@e%%cmnosjal9)6$4krj^5cs7=hd='

# Debug mode
DEBUG = False

# Allowed hosts
ALLOWED_HOSTS = ['*']

# Custom user model
AUTH_USER_MODEL = 'base.User'

# Language and time zone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('sw', 'Swahili'),
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory for collected static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Directory for development static files
]

# Use Whitenoise to serve static files in production
if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files (Cloudinary)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = 'https://res.cloudinary.com/drc3xiipg/'

# Installed apps
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base.apps.BaseConfig',
    'cloudinary_storage',
    'cloudinary',
    'rest_framework',
    'corsheaders',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware for serving static files
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database (PostgreSQL with Supabase)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.zzdoioliwmgvgfyoulsq',
        'PASSWORD': 'NyumbaChap',
        'HOST': 'aws-0-eu-central-1.pooler.supabase.com',
        'PORT': '5432',
    }
}

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Cloudinary settings
cloudinary.config(
    cloud_name='drc3xiipg',
    api_key='321181265585861',
    api_secret='KA2L_qJUCyBBZFcyeQDGzH1kfUo',
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'drc3xiipg',
    'API_KEY': '321181265585861',
    'API_SECRET': 'KA2L_qJUCyBBZFcyeQDGzH1kfUo',
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Root URL configuration
ROOT_URLCONF = 'core.urls'

# WSGI application
WSGI_APPLICATION = 'core.wsgi.application'

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True

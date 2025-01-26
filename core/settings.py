import os
import configparser
import cloudinary
import cloudinary_storage
import cloudinary.api
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')

BASE_DIR = Path(__file__).resolve().parent.parent


# SECRET_KEY = CONFIG['Django']['SECRET_KEY']
# SECRET_KEY = None
SECRET_KEY = '!5rt_gri@0-_0+#*nyb6+@e%%cmnosjal9)6$4krj^5cs7=hd='



DEBUG = True

#AUTH_USER_MODEL = CONFIG['Django']['AUTH_USER_MODEL']
AUTH_USER_MODEL = 'base.User'



ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# LANGUAGE_CODE = CONFIG['Django']['LANGUAGE_CODE']
LANGUAGE_CODE = 'en-us'




#language changer
USE_I18N = True
USE_L10N = True
USE_TZ = True
#language support
LANGUAGES = [
    ('en','English'),
    ('sw','Swahili'),
]



# TIME_ZONE = CONFIG['Django']['TIME_ZONE']
TIME_ZONE = 'UTC'


USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



#MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

#MEDIA_ROOT = BASE_DIR / 'static/images'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

CORS_ALLOW_ALL_ORIGINS = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }





# supabase database online_chat
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # Jina la database
        'USER': 'postgres.zzdoioliwmgvgfyoulsq',  # Jina la mtumiaji
        'PASSWORD': 'NyumbaChap',  # Badilisha kwa password yako halisi
        'HOST': 'aws-0-eu-central-1.pooler.supabase.com',  # URL ya server ya database
        'PORT': '5432',  # Port ya PostgreSQL (default ni 5432)
    }
}

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
    "corsheaders",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


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


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Cloudinary settings

cloudinary.config(
    cloud_name='drc3xiipg',  # Your Cloudinary cloud name
    api_key='321181265585861',   # Replace with your Cloudinary API key
    api_secret='KA2L_qJUCyBBZFcyeQDGzH1kfUo',  # Replace with your Cloudinary API secret
)




CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'drc3xiipg',  # Jina lako la Cloudinary
    'API_KEY': '321181265585861',  # API key yako
    'API_SECRET': 'KA2L_qJUCyBBZFcyeQDGzH1kfUo'  # API secret yako
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = 'https://res.cloudinary.com/drc3xiipg/'


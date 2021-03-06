"""
Django settings for kachelin project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import datetime
from dotenv import load_dotenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(dotenv_path=BASE_DIR + '/.env')

if (os.environ.get("SECERT_KEY")) == None:
    ENV_SECRET_KEY = os.environ['SECERT_KEY']
    ENV_DB_HOST = os.environ['DB_HOST']
    ENV_DB_NAME = os.environ['DB_NAME']
    ENV_DB_USER = os.environ['DB_USER']
    ENV_DB_PASSWORD = os.environ['DB_PASSWORD']
    ENV_DB_PORT = os.environ['DB_PORT']
else:
    ENV_SECRET_KEY = os.environ.get("SECERT_KEY")
    ENV_DB_HOST = os.environ.get("DB_HOST")
    ENV_DB_NAME = os.environ.get("DB_NAME")
    ENV_DB_USER = os.environ.get("DB_USER")
    ENV_DB_PASSWORD = os.environ.get("DB_PASSWORD")
    ENV_DB_PORT = os.environ.get("DB_PORT")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [".now.sh", "127.0.0.1"]

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'drf_yasg',
    'corsheaders',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'backend.apps.BackendConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kachelin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImtpZGV2ZWxvcDIiLCJleHAiOjE1OTA2OTQ5ODUsImVtYWlsIjoidXNlMjJyQGV4YW1wbGUuY29tIiwib3JpZ19pYXQiOjE1OTA2OTMxODV9.d08WJl6GjujtteBMXWmmvm2ZuAFuhDkWs9ps74OoZcU

WSGI_APPLICATION = 'kachelin.wsgi.application'

REST_USE_JWT = True

JWT_AUTH = { 
    'JWT_ALLOW_REFRESH': True, 
    'JWT_SECRET_KEY': SECRET_KEY, 
    'JWT_ALGORITHM': 'HS256', 
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=120), 
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7), 
}


REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'backend.serializers.user.LoginSerializer',
    'USER_DETAILS_SERIALIZER': 'backend.serializers.user.UserSerializer'
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': ENV_DB_HOST,
        'NAME': ENV_DB_NAME,
        'USER': ENV_DB_USER,
        'PASSWORD': ENV_DB_PASSWORD,
        'PORT': ENV_DB_PORT
    }
}

ACCOUNT_EMAIL_REQUIRED = False

ACCOUNT_EMAIL_VERIFICATION = 'none'

SWAGGER_SETTINGS = {
    'JSON_EDITOR': True,
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
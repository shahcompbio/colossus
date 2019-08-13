"""
Django settings for colossus project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/

Created on May 16, 2016

@author: Jafar Taghiyar (jtaghiyar@bccrc.ca)

Updated Oct 19, 2017 by Spencer Vatrt-Watts (github.com/Spenca)
"""
import datetime
import os
import sys

# Version
VERSION = "1.0.0"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('COLOSSUS_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('COLOSSUS_DEBUG', False))

ALLOWED_HOSTS = os.environ.get('COLOSSUS_ALLOWED_HOSTS', '127.0.0.1').split()


# Application definition

INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'account.apps.AccountConfig',
    'sisyphus.apps.SisyphusConfig',
    'dlp.apps.DlpConfig',
    'pbal.apps.PbalConfig',
    'tenx.apps.TenxConfig',
    'rest_framework',
    'django_filters', #filtering for rest_framework
    'django_extensions',
    'simple_history',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'crispy_forms',
    'storages',
    'corsheaders',
    # 'mod_wsgi.server',
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^.*$'

ROOT_URLCONF = 'colossus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                 os.path.join(BASE_DIR, 'templates')],
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

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        # for older django versions use ".postgresql_psycopg2"
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('COLOSSUS_POSTGRESQL_NAME'),
        'USER': os.environ.get('COLOSSUS_POSTGRESQL_USER'),
        'PASSWORD': os.environ.get('COLOSSUS_POSTGRESQL_PASSWORD'),
        'HOST': os.environ.get('COLOSSUS_POSTGRESQL_HOST', 'localhost'),
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Login url
LOGIN_URL = '/account/login/'

# Enabled security settings
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# Rest Framework Settings
REST_FRAMEWORK = {
    # pagination setting
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3600),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}


JIRA_URL = 'https://www.bcgsc.ca/jira/'

DEFAULT_FILE_STORAGE = 'colossus.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'colossus.custom_azure.AzureStaticStorage'



AZURE_ACCOUNT_NAME = "olympusbackups"
AZURE_ACCOUNT_KEY = os.environ.get('STORAGE_SECRET_KEY')

STATIC_URL = f'https://olympusbackups.blob.core.windows.net/colossus-static/'
MEDIA_URL = f'https://olympusbackups.blob.core.windows.net/colossus-media/'


STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
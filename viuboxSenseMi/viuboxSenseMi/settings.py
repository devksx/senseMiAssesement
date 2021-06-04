"""
Django settings for viuboxSenseMi project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pdkg@fx&-xa!6%ef@*q!!3ge#zeb*ajl(5_skub&&n$dyg^vjp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'tryviubox',
    'corsheaders',
    'gunicorn',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ALLOWED_HOSTS = ['sensemiheroku.herokuapp.com', '127.0.0.1/', '*']

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'https://googleads.g.doubleclick.net',
    "https://www.youtube.com", '*',
)
CORS_ALLOWED_ORIGINS = [
    "https://googleads.g.doubleclick.net",
    "http://localhost:8080",
    "https://www.youtube.com",
]
CORS_EXPOSE_HEADERS = ['*']
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = ['*',
                      # 'accept',
                      # 'accept-encoding',
                      # 'authorization',
                      # 'content-type',
                      # 'dnt',
                      # 'origin',
                      # 'user-agent',
                      # 'x-csrftoken',
                      # 'x-requested-with',
                      ]
CSRF_TRUSTED_ORIGINS = [
    "https://googleads.g.doubleclick.net",
    "http://localhost:8080",
    "https://www.youtube.com",
]
CORS_ALLOW_CREDENTIALS = True
# SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
ROOT_URLCONF = 'viuboxSenseMi.urls'

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
                # 'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'viuboxSenseMi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if DEBUG:
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #         'TEST_NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    #     }
    # }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'dfrcf0doul618o',
            'USER': 'tufvdsisisjvnk',
            'PASSWORD': 'a0f08b9f3034a8cc2288c98fc27c38e996276554f0096b6bba4df30fc20253a0',
            'HOST': 'ec2-174-129-225-160.compute-1.amazonaws.com',
            'PORT': '5432',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'dfrcf0doul618o',
            'USER': 'tufvdsisisjvnk',
            'PASSWORD': 'a0f08b9f3034a8cc2288c98fc27c38e996276554f0096b6bba4df30fc20253a0',
            'HOST': 'ec2-174-129-225-160.compute-1.amazonaws.com',
            'PORT': '5432',
        }
    }
    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

if DEBUG:
    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]

    STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

    MEDIA_DIR = '/media/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

else:
    PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'static'),
    )
    #  Add configuration for static files storage using whitenoise
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
    # import dj_database_url
    # prod_db = dj_database_url.config(conn_max_age=500)
    # DATABASES['default'].update(prod_db)
    django_heroku.settings(locals())

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from decouple import config, Csv
from pathlib import Path
import os
import decimal

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=True)

ALLOWED_HOSTS = config('ALLOWED_HOSTS',
                       cast=Csv(lambda x: x.strip().strip(',').strip()),
                       default='*')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.clientes',
    'apps.planos',
    'apps.financeiro',

    'django_extensions',
    'rangefilter',
    'constance',
    'constance.backends.database',
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

ROOT_URLCONF = 'vandog.urls'

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

WSGI_APPLICATION = 'vandog.wsgi.application'


# Database

from dj_database_url import parse as db_url

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
        cast=db_url
    )
}
# Password validation

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = config('STATIC_URL', default='/static/')
# STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'public', 'static'))
STATICFILES_DIRS = [
    os.path.abspath(os.path.join(BASE_DIR, 'public', 'static')),
]

FORCE_SCRIPT_NAME = config('FORCE_SCRIPT_NAME', default='')

USE_X_FORWARDED_HOST = True

# Constance

CONSTANCE_CONFIG = {
    'TAXA_DEBITO': (1.89, 'Taxa da maquininha na função débito'),
    'TAXA_CREDITO': (4.89, 'Taxa da maquininha na função crédito'),
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
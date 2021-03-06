"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


import os

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

DEBUG = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'session',
    'sekigae',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'


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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.User'

# custom authentication method
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                           'session.backends.FirebaseAuthBackend']

# logging
LOG_HANDLER_LEVEL = os.environ.get("DJANGO_LOG_HANDLER_LEVEL", "WARNING")
LOG_HANDLER_LEVEL_NULL = os.environ.get(
    "DJANGO_LOG_HANDLER_LEVEL_NULL", LOG_HANDLER_LEVEL)
LOG_HANDLER_LEVEL_CONSOLE = os.environ.get(
    "DJANGO_LOG_HANDLER_LEVEL_CONSOLE", LOG_HANDLER_LEVEL
)
LOG_HANDLER_LEVEL_MAIL = os.environ.get(
    "DJANGO_LOG_HANDLER_LEVEL_MAIL", LOG_HANDLER_LEVEL)
LOG_HANDLER_LEVEL_FILE = os.environ.get(
    "DJANGO_LOG_HANDLER_LEVEL_FILE", LOG_HANDLER_LEVEL)
LOG_HANDLER_FILE_PATH = os.environ.get(
    "DJANGO_LOG_HANDLER_FILE_PATH", "/var/log/django.log")
LOG_LOGGER_LEVEL = os.environ.get("DJANGO_LOG_LOGGER_LEVEL", "WARNING")
LOG_FILE_MAX_BYTES = int(os.environ.get(
    "DJANGO_LOG_FILE_MAX_BYTES", 1024 * 1024))
LOG_FILE_BACKUP_COUNT = int(os.environ.get("DJANGO_LOG_FILE_BACKUP_COUNT", 5))

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s'
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {},
    "handlers": {
        "null": {
            "level": LOG_HANDLER_LEVEL_NULL,
            "class": "logging.NullHandler",
        },
        "console": {
            "level": LOG_HANDLER_LEVEL_CONSOLE,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "mail": {
            "level": LOG_HANDLER_LEVEL_MAIL,
            "class": "django.utils.log.AdminEmailHandler",
        },
        "file": {
            "level": LOG_HANDLER_LEVEL_FILE,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_HANDLER_FILE_PATH,
            "formatter": "verbose",
            "maxBytes": LOG_FILE_MAX_BYTES,
            "backupCount": LOG_FILE_BACKUP_COUNT,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["null"],
            "propagate": True,
            "level": LOG_LOGGER_LEVEL,
        },
        "django.security.csrf": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
            "propagate": False,
        },
        "config": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
        },
        "account": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
        },
        "sekigae": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
        },
        "core": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
        },
        "session": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
        },
    },
}

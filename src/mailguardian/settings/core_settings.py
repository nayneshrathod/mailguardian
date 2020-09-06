"""
Django settings for MailGuardian project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import platform
from django.core.management.utils import get_random_secret_key


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'UNSECURE_SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
APP_HOSTNAME = platform.node()
APP_VERSION = '2.0.0'
LOCAL_CONFIG_VERSION = '0.0.0'
ALLOWED_HOSTS = [APP_HOSTNAME] if APP_HOSTNAME else []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'guardian',
    'django_premailer',
    'core',
    'frontend',
    'setup_wizard',
    'domains',
    'mail',
    'spamassassin',
    'lists',
    'reports',
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

ROOT_URLCONF = 'mailguardian.urls'

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

WSGI_APPLICATION = 'mailguardian.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mailguardian',
        'USER': 'mailguardian',
        'PASSWORD': 'mailguardian',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'sslmode': 'prefer'
        },
    }
}

# Make sure that we override the databse settings when running Travis/GitLab CI
if 'TRAVIS' in os.environ or 'GITLAB_CI' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql',
            'NAME':     'travisci',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }
elif 'GITLAB_CI' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql',
            'NAME':     'ci',
            'USER':     'postgres',
            'PASSWORD': 'postgres',
            'HOST':     'postgres',
            'PORT':     '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'core.User'
OLD_PASSWORD_FIELD_ENABLED = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    'locale'
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/assets/'
ASSETS_DIR = os.path.join(os.path.dirname(BASE_DIR), "assets")

# Guardian Authentication backends
# https://django-guardian.readthedocs.io/en/stable/configuration.html#configuration
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

# Django-Premailer
PREMAILER_OPTIONS = dict(remove_classes=True)

#MailGuardian specific settings
TMP_DIR = '/tmp'
MTA = 'postfix'
MTA_LOGFILE = '/var/log/maillog'
SENDMAIL_BIN = '/usr/sbin/sendmail'
POSTQUEUE_BIN = '/usr/sbin/postqueue'
AUDIT_LOGGING = True
API_ONLY = False
CONF_DIR = os.path.join(os.path.dirname(BASE_DIR), "configuration")

#MailScanner settings
MAILSCANNER_BIN = '/usr/sbin/MailScanner'
MAILSCANNER_CONFIG_DIR = '/etc/MailScanner'
MAILSCANNER_SHARE_DIR = '/usr/share/MailScanner'
MAILSCANNER_LIB_DIR = '/usr/lib/MailScanner'
MAILSCANNER_QUARANTINE_DIR = '/var/spool/MailScanner/quarantine'

# SpamAssassin settings
SALEARN_BIN = '/usr/bin/salearn'
SA_BIN = '/usr/bin/spamassassin'
SA_RULES_DIR = '/usr/share/spamassassin'
SA_PREF = MAILSCANNER_CONFIG_DIR+'/spamassassin.conf'

# Retention policy
RECORD_RETENTION = 60
AUDIT_RETENTION = 60
QUARANTINE_RETENTION = 60

# Branding
BRAND_NAME = 'MailGuardian'
BRAND_TAGLINE = 'Securing your email'
BRAND_LOGO = ''
BRAND_SUPPORT = 'https://github.com/khit93/mailguardian/issues'
BRAND_FEEDBACK = 'https://github.com/khit93/mailguardian-feedback'

# GeoIP
MAXMIND_DB_PATH = os.path.join(os.path.dirname(BASE_DIR), 'run')
MAXMIND_DB_FILE = os.path.join(MAXMIND_DB_PATH, 'GeoLite2.mmdb')
MAXMIND_ACCOUNT_API_KEY = False
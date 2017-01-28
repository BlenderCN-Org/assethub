"""
Django settings for assethub project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import re

from secret_settings import *
from email_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS=[]


# Application definition

INSTALLED_APPS = [
    # Main application
    'assets',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    # To use S3 storage
    'storages',
    # To enable translations of Application and Component descriptions
    'modeltranslation',
    'django_gravatar',
    # Markdown
    'markdown_deux',
    # Markdown editor
    'pagedown',
    # REST API
    'rest_framework',
    # Social networks authentication
    'social_django',
    'django_comments',
    # Tags for assets
    'taggit',
    # Autocomplete for tags
    'taggit_autosuggest',
    # Voting / rating / liking
    'vote',
    'notifications',
    # Configurable top menu
    'flatmenu'
]

SITE_ID=1

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GooglePlusAuth',
    'django.contrib.auth.backends.ModelBackend',
    )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'assethub.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'assets.context_processors.common_variables',
            ],
        },
    },
]

# CSS for markdown editor widget
PAGEDOWN_WIDGET_CSS=("assets/pagedown.css", )

COMMENTS_APP = "assets"

NOTIFICATIONS_USE_JSONFIELD=True

WSGI_APPLICATION = 'assethub.wsgi.application'

# Configuration for REST API framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# How long account activation links will be active
ACCOUNT_ACTIVATION_DAYS=3
# Redirect user to / after log out
LOGOUT_REDIRECT_URL="/"

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

LOCALE_PATHS = (BASE_DIR + "/locale", )
LANGUAGES = (
        ('en', 'English'),
        ('ru', 'Russian'),
    )
DEFAULT_LANGUAGE='en'
MODELTRANSLATION_DEFAULT_LANGUAGE='en'
MODELTRANSLATION_TRANSLATION_REGISTRY='assets.translation'
MODELTRANSLATION_AUTO_POPULATE=True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT='/static/'
STATIC_URL = '/static/'
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#MEDIA_ROOT='/up/'
MEDIA_URL='/media/'

# Use S3 to store media files uploaded by users
# Comment this out to use default filesystem storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# List of automatic thumbnailer classes
THUMBNAILER_CLASSES = ["assets.thumbnailers.ImageThumbnailer",
                       "assets.thumbnailers.KritaPresetThumbnailer",
                       "assets.thumbnailers.KritaBundleThumbnailer"
                      ]
DEFAULT_THUMBNAILER = None

DEFAULT_MAX_THUMB_SIZE = 300
DEFAULT_MAX_IMAGE_SIZE = 1024

# Settings for markdown
MARKDOWN_DEUX_STYLES = {
    "default": {
            "link_patterns": [
                # convert #123 to link to /asset/123/
                (re.compile(r'#(\d+)\b'), r"/asset/\1/"),
                # convert #hashtag to link to /tag/hashtag/
                (re.compile(r'#(\w+)\b'), r"/tag/\1/"),
                # convert @user to link to /accounts/profile/user/
                (re.compile(r'@([-\w]+)\b'), r"/accounts/profile/\1"),
            ],
            "extras": {
                "code-friendly": None,
                "demote-headers": 1,
                # its odd but for some reason we have to specify both "link-patterns" and "link_patterns"
                "link-patterns": None,
            },
        "safe_mode": "escape",
    }
}


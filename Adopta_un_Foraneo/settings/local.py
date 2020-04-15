from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adopta_foraneo',
        'USER': 'abulnes',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 3306
    }
}


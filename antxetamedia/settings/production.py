# -*- coding: utf-8 -*-
import json
from antxetamedia.settings.settings import *

with open('env.json') as e:
    env = json.load(e)

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = False

SECRET_KEY = env['SECRET_KEY']

CACHE_BACKEND = env['CACHE_BACKEND']
CACHE_MIDDLEWARE_SECONDS = 90
MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',
                    'django.middleware.gzip.GZipMiddleware') +\
                    MIDDLEWARE_CLASSES + \
                    ('django.middleware.http.ConditionalGetMiddleware',
                    'django.middleware.cache.FetchFromCacheMiddleware',
                    'antxetamedia.middleware.SSLRedirect',)

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env['DATABASE_NAME'],
            'USER': env['DATABASE_USER'],
            'PASSWORD': env['DATABASE_PASSWORD'],
            'HOST': '',
            'PORT': '',
            }
        }

MEDIA_ROOT = env['MEDIA_ROOT']
STATIC_ROOT = env['STATIC_ROOT']
SSL_URLS = (r'/admin/',)


ADMINS = (
        ('Unai Zalakain', '{0}@{1}.{2}'.format('contact', 'unaizalakain', 'info')),
)
MANAGERS = ADMINS

EMAIL_SUBJECT_PREFIX = '[AM]'
EMAIL_HOST = env['EMAIL_HOST']
EMAIL_HOST_USER = env['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = env['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = env['DEFAULT_FROM_EMAIL']
SERVER_EMAIL = env['SERVER_EMAIL']


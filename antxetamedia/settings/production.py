from django.conf import global_settings as SETTINGS
from os.path import dirname, join
DIR = dirname(__file__)


#SITE
SITE_ID = 1
SECRET_KEY = 'f-p9*m*-r%#em9n5ge!6kj)@rlda7_73-**3cyjyye_uc-1uyc'


#DEBUG
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG


#EPOSTAK
ADMINS = ()
MANAGERS = ADMINS


#DATUBASEA
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(DIR, 'db'),                      
        'USER': '',                      
        'PASSWORD': '',                  
        'HOST': '',                      
        'PORT': '',                      
    }
}


#I18N
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'eu'
FIRST_DAY_OF_WEEK = 1
USE_I18N = True
USE_L10N = False
DATE_INPUT_FORMATS = SETTINGS.DATE_INPUT_FORMATS + ('%Y/%m/%d',)


#PATHS
ROOT_URLCONF = 'antxetamedia.urls'
STATIC_URL = '/media/'
MEDIA_ROOT = join(dirname(DIR), 'static')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'
DAJAXICE_MEDIA_PREFIX = 'ajax'


#TEMPLATEAK
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
USE_X_FORWARDED_HOST = True
TEMPLATE_DIRS = (join(DIR, 'templates'),)
TEMPLATE_CONTEXT_PROCESSORS = SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'antxetamedia.structure.context_processors.nodes_on_menu',
        'antxetamedia.structure.context_processors.root_nodes',
        'antxetamedia.recordings.context_processors.news_categories',
        'antxetamedia.misc.context_processors.headlines',
        'antxetamedia.misc.context_processors.banner',
        )


#APLIKAZIOAK
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.sitemaps',

    'autoslug',
    'colorful',
    'taggit',
    'taggit_templatetags',
    'dajaxice',
    'haystack',
    'south',
    'uni_form',

    'antxetamedia.multimedia',
    'antxetamedia.structure',
    'antxetamedia.recordings',
    'antxetamedia.agenda',
    'antxetamedia.programming',
    'antxetamedia.misc',
)

#PROGRAMMING
PROGRAMMING_SPACE = 30

#GRAPPELLI
GRAPPELLI_ADMIN_TITLE = 'AntxetaMedia.info'
GRAPPELLI_ADMIN_URL = '/admin'
GRAPPELLI_INDEX_DASHBOARD = 'antxetamedia.dashboard.CustomIndexDashboard'

#HAYSTACK
HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'xapian_backend.XapianEngine',
            'PATH': join(DIR, 'xapian'),
            }
        }
HAYSTACK_DEFAULT_OPERATOR = 'AND'

SSL_URLS = ()

#S3
S3_HOST = 's3.us.archive.org'
S3_METADATA = {
        'x-archive-meta-mediatype': 'audio',
        'x-archive-meta-collection': 'opensource_audio',
        }

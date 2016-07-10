from django.conf import global_settings as SETTINGS
from os.path import dirname, join
DIR = dirname(dirname(__file__))


#I18N
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'eu'
FIRST_DAY_OF_WEEK = 1
USE_I18N = True
LOCALE_PATHS = [join(DIR, 'locale')]
USE_L10N = False
USE_TZ = True
DATE_INPUT_FORMATS = SETTINGS.DATE_INPUT_FORMATS + ('%Y/%m/%d',)


#PATHS
ROOT_URLCONF = 'antxetamedia.urls'
DAJAXICE_MEDIA_PREFIX = 'ajax'

STATIC_URL = '/static/'
STATIC_ROOT = join(DIR, 'assets')
MEDIA_URL = '/media/'
MEDIA_ROOT = join(DIR, 'media')
ADMIN_MEDIA_PREFIX = '/admin_media/'
STATICFILES_DIRS = [join(DIR, 'static')]

USE_X_FORWARDED_HOST = True
MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (join(DIR, 'templates'),)
TEMPLATE_CONTEXT_PROCESSORS = SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'antxetamedia.structure.context_processors.nodes_on_menu',
        'antxetamedia.structure.context_processors.root_nodes',
        'antxetamedia.recordings.context_processors.news_categories',
        'antxetamedia.misc.context_processors.headlines',
        'antxetamedia.misc.context_processors.banner',
        'antxetamedia.projects.context_processors.projects',
        )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.sitemaps',

    'autoslug',
    'colorful',
    'dajaxice',
    'haystack',
    'south',
    'uni_form',
    'markitup',
    'sorl.thumbnail',

    'antxetamedia.multimedia',
    'antxetamedia.structure',
    'antxetamedia.recordings',
    'antxetamedia.agenda',
    'antxetamedia.programming',
    'antxetamedia.misc',
    'antxetamedia.projects',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


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
HAYSTACK_XAPIAN_PATH = HAYSTACK_CONNECTIONS['default']['PATH']

SSL_URLS = ()

#S3
S3_HOST = 's3.us.archive.org'
S3_METADATA = {
        'x-archive-meta-mediatype': u'audio',
        'x-archive-meta-collection': u'opensource_audio',
        }

MARKITUP_FILTER = ('markdown.markdown', {})
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/markitup'
MARKITUP_AUTO_PREVIEW = True

JQUERY_URL = 'js/jquery.js'

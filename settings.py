import os
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_BASEURL = '/'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = True

MEDIA_URL = SITE_BASEURL + ''
ADMIN_MEDIA_PREFIX = '/admin/media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
        os.path.join(SITE_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'image',

	# south, for migrations
	'south',
)

IMAGE_ID_OFFSET = 0
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'

# import local settings (if it exists) and override these things.
try:
    from local_settings import *
except:
    pass


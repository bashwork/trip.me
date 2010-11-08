#------------------------------------------------------------------------------ 
# Default Project Root
#------------------------------------------------------------------------------ 
import os,sys
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

#------------------------------------------------------------------------------ 
# Django settings for prototype project.
#------------------------------------------------------------------------------ 
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Galen Collins', 'x@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, 'db/database'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#------------------------------------------------------------------------------ 
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#------------------------------------------------------------------------------ 
TIME_ZONE = 'America/Chicago'

#------------------------------------------------------------------------------ 
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#------------------------------------------------------------------------------ 
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

#------------------------------------------------------------------------------ 
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
#------------------------------------------------------------------------------ 
USE_I18N = True

#------------------------------------------------------------------------------ 
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
#------------------------------------------------------------------------------ 
USE_L10N = True

#------------------------------------------------------------------------------ 
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#------------------------------------------------------------------------------ 
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static/')

#------------------------------------------------------------------------------ 
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#------------------------------------------------------------------------------ 
MEDIA_URL = '/static/'

#------------------------------------------------------------------------------ 
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#------------------------------------------------------------------------------ 
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = 'j2=%(9*x)q$kktnm^qx3mgq7r8vmq931z!lru+ivr3$*lkyy$!'

#------------------------------------------------------------------------------ 
# List of callables that know how to import templates from various sources.
#------------------------------------------------------------------------------ 
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
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'django_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'tripme.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.flatpages',
    #'debug_toolbar',
    'alphafilter',
    'tripme.guides',
)

#------------------------------------------------------------------------------ 
# Global Context Settings
#------------------------------------------------------------------------------ 
import django.conf.global_settings as DEFAULT_SETTINGS
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'context_processors.aggregator_conext',
)

"""
Django settings for testproj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_6j!azi$&%qk(5re8j^j%a#lie7!-s9y41e@1a^f5@)elb3e7k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
#    'allauth',
#    'allauth.account',
#    'allauth.socialaccount',
#    'allauth.socialaccount.providers.linkedin_oauth2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'testproj.urls'

WSGI_APPLICATION = 'testproj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES = {
#  'default': {
#    'ENGINE': 'django.db.backends.postgresql_psycopg2',
#    'NAME': 'd3hhnp67s1gtmm',
#    'HOST': 'ec2-54-204-31-13.compute-1.amazonaws.com',
#    'PORT': 5432,
#    'USER': 'xneoghfidyhzzk',
#    'PASSWORD': 'pBULwfWiA54rcuydOMsIasJZ_2'
#  }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
import os.path
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    # Required by allauth template tags
#    "django.core.context_processors.request",
#    'django.contrib.auth.context_processors.auth',
#    # allauth specific context processors
#    "allauth.account.context_processors.account",
#    "allauth.socialaccount.context_processors.socialaccount",
#)
#AUTHENTICATION_BACKENDS = (
#    # Needed to login by username in Django admin, regardless of `allauth`
#    "django.contrib.auth.backends.ModelBackend",
#
#    # `allauth` specific authentication methods, such as login by e-mail
#    "allauth.account.auth_backends.AuthenticationBackend",
#)

#SITE_ID = 1



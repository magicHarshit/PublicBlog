import  os

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('admin', 'admin@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'myblog',  # Or path to database file if using sqlite3.
        'USER': 'root',   # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'America/Bogota'

LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = '/'



STATIC_ROOT = ''
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH,'static'),
)
CKEDITOR_UPLOAD_PATH = '/home/harshit/workspace/code/myblog/wsgi/openshift/static/'
#todo change

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

default_keys = {'SECRET_KEY':'o3e(t&1l8(1j_!gn@m+r=km28&!zdazm2m)6n@eze6h=f$nq2#'}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'ckeditor',
    'post',
    'social_auth',
    'rest_framework',
)

use_keys = default_keys

SECRET_KEY = use_keys['SECRET_KEY']

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Full',
        'height': 300,
        'width': 900,
    },
}

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'

AUTHENTICATION_BACKENDS = (
  'social_auth.backends.google.GoogleOAuth2Backend',
  # 'social_auth.backends.contrib.github.GithubBackend',
  'django.contrib.auth.backends.ModelBackend',
)


TEMPLATE_CONTEXT_PROCESSORS = (
  "social_auth.context_processors.social_auth_by_type_backends",
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.static',
)

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UID_LENGTH = 200
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16

SOCIAL_AUTH_ENABLED_BACKENDS = ('google',)


# GITHUB_API_KEY = ''
# GITHUB_API_SECRET = ''

GOOGLE_OAUTH2_CLIENT_ID = '404204672487.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'BNwr39QqbazblI0yTYtfLuHw'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework.authentication.SessionAuthentication',
    )
}

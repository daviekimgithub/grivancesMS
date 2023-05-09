"""
Django settings for grivances project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
# import environ
# env = environ.Env()
# environ.Env.read_env()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^e=8$yfkkclnxd=#bcaf019t=@w^#-!gxki=awdm8^5f2s(w&b'
# SECRET_KEY = env('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SUIT_CONFIG = {
    'ADMIN_NAME': 'My Site Admin',
    'HEADER_DATE_FORMAT': 'l, F j, Y',
    'HEADER_TIME_FORMAT': 'H:i',
    'MENU': (
        'sites',
        {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    ),
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'support': 'icon-question-sign',
    },
    'MENU_OPEN_FIRST_CHILD': True,
    'MENU_EXCLUDE': ('auth.group',),
    'LIST_PER_PAGE': 15,
    'SHOW_FULLSCREEN': True,
    'MENU_COLLAPSE': False,
    'HEADER_COLOR': 'black',
    'HEADER_ADMIN_NAME': 'DARK MODE',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'LIST_FILTER_THUMBNAIL': True,
    'LIST_FILTER_COLLAPSE': True,
    'LIST_FILTER_NON_ADMIN_COLLAPSE': True,
    'MENU_ORDER': (
        ('sites',),
        ('auth', ('user', 'group')),
        ('support',),
    ),
    'SEARCH_USE_DISTINCT': True,
    'MENU_BADGE': True,
    'MENU_BADGE_BG': 'red',
    'MENU_BADGE_FG': 'white',
    'MENU_UNHIDE': True,
    'MENU_UNHIDE_FIRST_CHILD': True,
    'MENU_STICKY': True,
    'MENU_COMPACT': True,
    'MENU_REVERSE': True,
    'MENU_ICONS_EXTRA': {
        'auth.user': 'icon-user',
        'auth.group': 'icon-th-large',
    },
    'THEME': 'dark',
}



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'server.apps.ServerConfig',
    'rest_framework',
    'admin_interface',
    'suit',
    'colorfield',
]

# ADMIN_INTERFACE_THEME = 'black'

# ADMIN_INTERFACE_SETTINGS = {
#     'theme': 'black',
#     'title': 'My Admin Panel',
#     'favicon': '/static/img/favicon.png',
#     'logo': '/static/img/logo.png',
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grivances.urls'

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

WSGI_APPLICATION = 'grivances.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
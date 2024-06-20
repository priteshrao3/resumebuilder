
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eq*%976sngu+3bxg*=jv)=_^j18ebdx=ia5fn=4=+^9t-lx9^s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_HOST_USER = 'enquiry.prwebtechno@gmail.com'
EMAIL_HOST_PASSWORD = 'ckhz weae tuss mlpe'
EMAIL_USE_TLS = True




# Application definition

INSTALLED_APPS = [
    'material',
    'material.admin',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.custom_middleware.AutoLoginMiddleware',
]

ROOT_URLCONF = 'resumeproject.urls'

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

WSGI_APPLICATION = 'resumeproject.wsgi.application'


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
STATIC_ROOT = "resumeproject/static/"


MEDIA_URL = '/media/'
MEDIA_ROOT = 'resumeproject/media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Material Admin Settings And Icons Start
MATERIAL_ADMIN_SITE = {
    'HEADER':  _('Welcome To Prwebtechno'),
    'TITLE':  _('prwebtechno'), 
    'FAVICON':  '/images/feviconicon.png', 
    'MAIN_BG_COLOR':  '#334924',
    'MAIN_HOVER_COLOR':  '#2B4424', 
    'PROFILE_PICTURE':  '/images/feviconicon.png', 
    # 'PROFILE_BG':  'img/welcomeadmin.jpg',
    'LOGIN_LOGO':  '/images/feviconicon.png', 
    # 'LOGOUT_BG':  '/images/logo.webp', 
    'SHOW_THEMES':  True, 
    'TRAY_REVERSE': True, 
    'NAVBAR_REVERSE': True, 
    
    'SHOW_COUNTS': True, 
      'APP_ICONS': { 
        'sites': 'send',
        'core': 'assignment',
    },
    'MODEL_ICONS': {  
        'site': 'contact_mail',
        'user': 'person_pin',
    },
}
# Material Admin Settings And Icons End

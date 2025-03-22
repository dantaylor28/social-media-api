# """
# Django settings for socialmediaapi project.

# Generated by 'django-admin startproject' using Django 5.1.6.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.1/ref/settings/
# """

# from pathlib import Path
# import os
# import dj_database_url
# from datetime import timedelta

# if os.path.exists('env.py'):
#     import env

# CLOUDINARY_STORAGE = {
#     'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
# }
# MEDIA_URL = '/media/'
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),   # Short-lived access token
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=7),     # Refresh token valid for 7 days
#     "ROTATE_REFRESH_TOKENS": True,                   # Get a new refresh token with each refresh
#     "BLACKLIST_AFTER_ROTATION": True,                # Prevent reuse of old refresh tokens
#     "AUTH_HEADER_TYPES": ("Bearer",),                # Use Bearer token authentication
#     "COOKIE_NAME": "my-app-auth",
#     "REFRESH_COOKIE_NAME": "my-refresh-token",
#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
# }

# # REST_FRAMEWORK = {
# #     'DEFAULT_PERMISSION_CLASSES': [
# #         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
# #     ],
# #     'DEFAULT_PAGINATION_CLASS':
# #         'rest_framework.pagination.PageNumberPagination',
# #     'PAGE_SIZE': 10,
# #     'DATETIME_FORMAT': '%d %B %Y',
# #     'DEFAULT_AUTHENTICATION_CLASSES': [(
# #         'rest_framework.authentication.SessionAuthentication'
# #         if 'DEV' in os.environ
# #         else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
# #         # Test to fix sign in error
# #         # else 'dj_rest_auth.authentication.AllAuthJWTAuthentication'
# #     )]
# # }

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     ],
#     'DEFAULT_PAGINATION_CLASS':
#         'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10,
#     'DATETIME_FORMAT': '%d %B %Y',
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication'
#         if 'DEV' in os.environ
#         else 'rest_framework_simplejwt.authentication.JWTAuthentication'
#     ]
# }

# if 'DEV' not in os.environ:
#      REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
#          'rest_framework.renderers.JSONRenderer',
#      ]

# REST_USE_JWT = True
# JWT_AUTH_SECURE = True
# JWT_AUTH_COOKIE = 'my-app-auth'
# JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
# JWT_AUTH_SAMESITE = 'None'
# JWT_AUTH_HTTPONLY = True

# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'socialmediaapi.serializers.CurrentUserSerializer'
# }


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv('SECRET_KEY')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = 'DEV' in os.environ

# ALLOWED_HOSTS = [
#     'localhost', '127.0.0.1',
# os.environ.get('ALLOWED_HOST'),
# ]


# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'cloudinary_storage',
#     'django.contrib.staticfiles',
#     'cloudinary',
#     'rest_framework',
#     'django_filters',
#     'rest_framework.authtoken',
#     'dj_rest_auth',
#     'django.contrib.sites',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'dj_rest_auth.registration',
#     'corsheaders',

#     'posts',
#     'profiles',
#     'pins',
#     'comments',
#     'followers',
#     'comment_likes',
#     'categories',
# ]

# SITE_ID = 1
# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     # Had to add below line to fix a random error with allauth
#     'allauth.account.middleware.AccountMiddleware',
# ]

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
# ]
# # if 'CLIENT_ORIGIN' in os.environ:
# #     CORS_ALLOWED_ORIGINS.append(os.environ.get('CLIENT_ORIGIN'))

# # if 'CLIENT_ORIGIN_DEV' in os.environ:
# #     CORS_ALLOWED_ORIGINS.append(os.environ.get('CLIENT_ORIGIN_DEV'))

# CORS_ALLOW_CREDENTIALS = True

# ROOT_URLCONF = 'socialmediaapi.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'socialmediaapi.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# if 'DEV' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
#     DATABASES = {
#         'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
#     }


# # Password validation
# # https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/5.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'








from pathlib import Path
import os
import dj_database_url
from datetime import timedelta

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

BASE_DIR = Path(__file__).resolve().parent.parent

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),  # Short-lived access token
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),  # Refresh token valid for 7 days
    "ROTATE_REFRESH_TOKENS": True,  # New refresh token each time
    "BLACKLIST_AFTER_ROTATION": True,  # Prevent reuse of old refresh tokens
    "AUTH_HEADER_TYPES": ("Bearer",),  # Use Bearer tokens
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %B %Y',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'rest_framework_simplejwt.authentication.JWTAuthentication'
    ]
}

if 'DEV' not in os.environ:
     REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
         'rest_framework.renderers.JSONRenderer',
     ]

# Use JWT-based authentication for dj-rest-auth
REST_USE_JWT = True
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'socialmediaapi.serializers.CurrentUserSerializer'
}

# Enable refresh token via cookies
REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "my-app-auth",  # Access token cookie name
    "JWT_AUTH_REFRESH_COOKIE": "my-refresh-token",  # Refresh token cookie name
}

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True  # Required for cookies!

ROOT_URLCONF = 'socialmediaapi.urls'

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

WSGI_APPLICATION = 'socialmediaapi.wsgi.application'

if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

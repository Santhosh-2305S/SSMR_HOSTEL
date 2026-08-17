"""
Django settings for hostel_management project.

Production configuration for Render deployment.
"""

from pathlib import Path
import os

import dj_database_url


# ==========================================================
# BASE DIRECTORY
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================================
# SECURITY
# ==========================================================

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-development-only-change-this-key",
)


# ==========================================================
# DEBUG
# ==========================================================

DEBUG = (
    os.environ.get(
        "DJANGO_DEBUG",
        "True",
    ).lower()
    == "true"
)


# ==========================================================
# ALLOWED HOSTS
# ==========================================================

allowed_hosts = os.environ.get(
    "DJANGO_ALLOWED_HOSTS",
    "127.0.0.1,localhost",
)


render_hostname = os.environ.get(
    "RENDER_EXTERNAL_HOSTNAME"
)


ALLOWED_HOSTS = [
    host.strip()
    for host in allowed_hosts.split(",")
    if host.strip()
]


if render_hostname:
    ALLOWED_HOSTS.append(
        render_hostname
    )


# ==========================================================
# APPLICATIONS
# ==========================================================

INSTALLED_APPS = [

    "django.contrib.admin",

    "django.contrib.auth",

    "django.contrib.contenttypes",

    "django.contrib.sessions",

    "django.contrib.messages",

    "django.contrib.staticfiles",

    "hostel",

]


# ==========================================================
# MIDDLEWARE
# ==========================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]


# ==========================================================
# URL CONFIGURATION
# ==========================================================

ROOT_URLCONF = "hostel_management.urls"


# ==========================================================
# TEMPLATES
# ==========================================================

TEMPLATES = [

    {

        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

        "DIRS": [

            BASE_DIR
            / "hostel_management"
            / "templates",

        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.debug",

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]


# ==========================================================
# WSGI
# ==========================================================

WSGI_APPLICATION = (
    "hostel_management.wsgi.application"
)


# ==========================================================
# DATABASE
# ==========================================================

DATABASE_URL = os.environ.get(
    "DATABASE_URL"
)


if DATABASE_URL:

    DATABASES = {

        "default": dj_database_url.config(

            default=DATABASE_URL,

            conn_max_age=600,

            ssl_require=not DEBUG,

        )

    }

else:

    DATABASES = {

        "default": {

            "ENGINE":
                "django.db.backends.sqlite3",

            "NAME":
                BASE_DIR / "db.sqlite3",

        }

    }


# ==========================================================
# PASSWORD VALIDATION
# ==========================================================

AUTH_PASSWORD_VALIDATORS = [

    {

        "NAME":
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator",

    },

    {

        "NAME":
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator",

    },

    {

        "NAME":
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator",

    },

    {

        "NAME":
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator",

    },

]


# ==========================================================
# INTERNATIONALIZATION
# ==========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# ==========================================================
# STATIC FILES
# ==========================================================

STATIC_URL = "/static/"


STATICFILES_DIRS = [

    BASE_DIR
    / "hostel_management"
    / "static",

]


STATIC_ROOT = (
    BASE_DIR / "staticfiles"
)


STORAGES = {

    "staticfiles": {

        "BACKEND":
            "whitenoise.storage."
            "CompressedManifestStaticFilesStorage",

    },

}


# ==========================================================
# MEDIA FILES
# ==========================================================

MEDIA_URL = "/media/"


MEDIA_ROOT = (
    BASE_DIR
    / "hostel_management"
    / "media"
)


# ==========================================================
# LOGIN / LOGOUT
# ==========================================================

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "dashboard"

LOGOUT_REDIRECT_URL = "login"


# ==========================================================
# DEFAULT PRIMARY KEY
# ==========================================================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)


# ==========================================================
# CSRF TRUSTED ORIGINS
# ==========================================================

csrf_origins = os.environ.get(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    "",
)


CSRF_TRUSTED_ORIGINS = [

    origin.strip()

    for origin in csrf_origins.split(",")

    if origin.strip()

]


# ==========================================================
# PRODUCTION SECURITY
# ==========================================================

if not DEBUG:

    SECURE_SSL_REDIRECT = True

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = "DENY"

    SECURE_HSTS_SECONDS = 31536000

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

    SECURE_REFERRER_POLICY = (
        "strict-origin-when-cross-origin"
    )
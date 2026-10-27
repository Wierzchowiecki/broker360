"""
Django settings for the Broker 360 project.
"""

import os

from pathlib import Path


# Główny folder projektu

BASE_DIR = Path(__file__).resolve().parent.parent


# Ustawienia bezpieczeństwa dla wersji lokalnej

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-local-development-only",
)

DEBUG = os.environ.get(
    "DJANGO_DEBUG",
    "True",
).lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        "DJANGO_ALLOWED_HOSTS",
        "127.0.0.1,localhost",
    ).split(",")
    if host.strip()
]


# Aplikacje używane w projekcie

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "properties.apps.PropertiesConfig",
    "contact.apps.ContactConfig",
]


# Elementy pośredniczące Django

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Główny plik adresów URL

ROOT_URLCONF = "config.urls"


# Ustawienia szablonów HTML

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Ustawienia serwera Django

WSGI_APPLICATION = "config.wsgi.application"


# Baza danych SQLite
# Później zastąpimy ją bazą MySQL.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Sprawdzanie bezpieczeństwa haseł

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# Język i strefa czasowa

LANGUAGE_CODE = "pl"

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_TZ = True


# Pliki statyczne: CSS, JavaScript i obrazy

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# Automatyczne klucze główne tabel SQL

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------
# Sécurité
# -------------------

# ⚠️ DEBUG désactivé par défaut en prod, activé seulement si variable DJANGO_DEBUG=True
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# ⚠️ La clé secrète doit être injectée depuis Railway (Variables d'env)
SECRET_KEY = os.getenv("SECRET_KEY", "insecure-secret-key")

# Domaine Railway + localhost pour tests
ALLOWED_HOSTS = [
    "web-production-79226.up.railway.app",
    "127.0.0.1",
    "localhost"
]

# CSRF → obligatoire pour éviter l’erreur 403
CSRF_TRUSTED_ORIGINS = [
    "https://web-production-79226.up.railway.app"
]

# -------------------
# Applications
# -------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'monportfoliodjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'portfolio/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'monportfoliodjango.wsgi.application'

# -------------------
# Base de données (SQLite en local, Railway peut utiliser Postgres si besoin)
# -------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------
# Validation des mots de passe
# -------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------
# Internationalisation
# -------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------
# Fichiers statiques et médias
# -------------------
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / "portfolio/static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------
# Configuration Email (⚠️ pense à mettre des variables d’environnement)
# -------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "ton.email@gmail.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "motdepasse_app")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
RECIPIENT_ADDRESS = os.getenv("RECIPIENT_ADDRESS", "ton.email@gmail.com")

# LibraryProject/LibraryProject/settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Debug & Hosts ---------------------------------------------------------
# Always run with DEBUG=False in production.
DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() in ("1", "true", "yes")

# Set ALLOWED_HOSTS with comma-separated env var or explicit list
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# --- HTTPS / HSTS / Cookie Settings ---------------------------------------
# Redirect all HTTP requests to HTTPS (enforce HTTPS)
# In development you may want this False; use env var to control.
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "True").lower() in ("1", "true", "yes")

# HTTP Strict Transport Security (HSTS)
# 31536000 = 1 year. Enable with caution; ensure your site is fully HTTPS before setting large values.
SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "31536000"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.getenv("SECURE_HSTS_INCLUDE_SUBDOMAINS", "True").lower() in ("1", "true", "yes")
SECURE_HSTS_PRELOAD = os.getenv("SECURE_HSTS_PRELOAD", "True").lower() in ("1", "true", "yes")

# Ensure cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Make session cookie inaccessible to JavaScript
SESSION_COOKIE_HTTPONLY = True
# CSRF_COOKIE_HTTPONLY is typically False so client-side JS can read cookie if needed for AJAX.
# Only set True if your front-end doesn't need to read the cookie directly.
CSRF_COOKIE_HTTPONLY = False

# --- Browser protections / headers ----------------------------------------
# Prevent the browser from MIME-sniffing responses away from declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent the site from being framed (clickjacking protection)
X_FRAME_OPTIONS = "DENY"

# When behind a proxy/load balancer (e.g., nginx), tell Django how to detect HTTPS:
# Ensure your proxy sets the X-Forwarded-Proto header. Example:
#    proxy_set_header X-Forwarded-Proto $scheme;
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# --- Content Security Policy (optional) -----------------------------------
# If you use django-csp, configure CSP_* settings here. Otherwise set CSP
# header in your webserver or use a small middleware.
# Example minimal:
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)          # add any trusted CDNs here
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")  # avoid 'unsafe-inline' if possible
CSP_IMG_SRC = ("'self'", "data:")
CSP_CONNECT_SRC = ("'self'",)

# --- Misc / Media ---------------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --- Middleware & Installed apps (ensure SecurityMiddleware is present) ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",       # uses SECURE_* settings
    # If you implement custom CSP middleware, add it here:
    # "LibraryProject.middleware.ContentSecurityPolicyMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # sets X-Frame-Options header
]

INSTALLED_APPS = [
    # default django apps...
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # your apps
    "bookshelf",
    # optionally "csp" if you install django-csp
]

# --- Logging: surface security issues in prod logs -------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "WARNING"},
}

# NOTE: Use environment variables or a secrets manager for keys and secrets.

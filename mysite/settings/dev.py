from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '68d5+@8s+p^n%(2)$3$*9(2r813z0ty$vy@6x#hjyj=i(g(b68'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar'
]

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")


MIDDLEWARE = MIDDLEWARE + [
  
    'debug_toolbar.middleware.DebugToolbarMiddleware',
   
]

try:
    from .local import *
except ImportError:
    pass

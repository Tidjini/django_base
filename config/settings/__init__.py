from decouple import config
from django.core.exceptions import ImproperlyConfigured
import dj_database_url


def get_environ_variable(var_name):
    try:
        return config(var_name)
    except:
        message = f'{var_name} not exist in your environment.'
        raise ImproperlyConfigured(message)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


SECRET_KEY = get_environ_variable('SECRET_KEY')

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

environment = config("ENV")
# choose any of keys for me i set development and production in .env file
if environment.lower() == "development":
    from .dev import *
elif environment.lower() == "test":
    from .test import *
elif environment.lower() == "production":
    from .prod import *
else:
    from .base import *

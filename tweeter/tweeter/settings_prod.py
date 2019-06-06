from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tweet',
        'USER': 'nurs',
        'PASSWORD': 'nurs123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

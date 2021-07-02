"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from dotenv import load_dotenv
load_dotenv(os.path.join(BASE_DIR, ".env"))

envstate = os.getenv('ENV_STATE')
if envstate == 'production':
    # settings/production.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'config.settings.production')
elif envstate == 'staging':
    # settings/staging.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.staging')
else:
    # settings/local.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')


application = get_wsgi_application()

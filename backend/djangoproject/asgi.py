"""
ASGI config for djangoproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/

Allows for optional Asynchronous Server Gateway Interface to be run
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

application = get_asgi_application()

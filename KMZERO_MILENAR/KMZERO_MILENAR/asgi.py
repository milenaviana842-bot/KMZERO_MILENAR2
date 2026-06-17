"""
ASGI config for KMZERO_MILENAR project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from dj_static import Cling, MediaCling
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KMZERO_MILENAR.settings")

application = Cling(MediaCling(get_asgi_application()))
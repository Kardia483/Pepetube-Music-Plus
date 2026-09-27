"""
Configuración ASGI para el proyecto pepetube_music_plus.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pepetube_music_plus.settings")

application = get_asgi_application()

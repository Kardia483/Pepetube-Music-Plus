"""
Configuración WSGI para el proyecto pepetube_music_plus.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pepetube_music_plus.settings")

application = get_wsgi_application()

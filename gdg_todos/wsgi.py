"""WSGI config for todos project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gdg_todos.settings')

application = get_wsgi_application()

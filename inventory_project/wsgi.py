"""
WSGI config for inventory_project.

This module contains the WSGI application used by Django's development server and any WSGI-compatible web server.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_project.settings')

application = get_wsgi_application()

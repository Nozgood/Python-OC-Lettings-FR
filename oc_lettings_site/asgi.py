"""
Module: asgi.py
Description: This module contains the ASGI application used for serving the
Django project.

Details:
    - It sets the default settings module for the 'oc_lettings_site' project.
    - It initializes the ASGI application to be used by ASGI servers.

Usage:
    This module is used to configure and create an ASGI application instance
    that can be used by any ASGI server to serve the Django project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()

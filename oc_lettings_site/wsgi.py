"""
Module: wsgi.py
Description: This module contains the WSGI application used for serving the
Django project.

Details:
    - It sets the default settings module for the 'oc_lettings_site' project.
    - It initializes the WSGI application to be used by WSGI servers.

Usage:
    This module is used to configure and create a WSGI application instance
    that can be used by any WSGI server to serve the Django project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()

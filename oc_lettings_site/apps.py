"""
Module: apps.py
Description: This module contains the configuration class for the
'oc_lettings_site' application.

Classes:
    - OCLettingsSiteConfig: Configuration class for the
    'oc_lettings_site' application.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
        Configuration class for the 'oc_lettings_site' application.

        Attributes:
            name (str): The name of the application.
    """
    name = 'oc_lettings_site'

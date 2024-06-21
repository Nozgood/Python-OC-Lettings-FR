"""
Module: apps.py
Description: This module contains the configuration class for the
'lettings' application.

Classes:
    - LettingsConfig: Configuration class for the 'lettings' application.
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
        Configuration class for the 'lettings' application.

        Attributes:
            name (str): The name of the application.
    """
    name = 'lettings'

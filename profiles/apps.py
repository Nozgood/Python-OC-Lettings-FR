"""
Module: apps.py
Description: This module contains the configuration class for the
'profiles' application.

Classes:
    - ProfilesConfig: Configuration class for the 'profiles' application.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
        Configuration class for the 'profiles' application.

        Attributes:
            name (str): The name of the application.
        """

    name = 'profiles'

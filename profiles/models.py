"""
Module: models.py
Description: This module contains the Django model for managing user profiles.

Class:
    - Profile: A model representing a user's profile,
    which includes a reference to the user and his/her favorite city.

Details:
    - The Profile model establishes a one-to-one relationship with the
    User model from Django's authentication system.
    - Each Profile object is linked to a unique User object,
    and includes an optional favorite city field.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
        A Django model representing a user's profile.

        Attributes:
            user (User): A one-to-one relationship with the User model.
            When the associated User is deleted, the Profile is also deleted.
            favorite_city (str): An optional field for the user's favorite city,
            with a maximum length of 64 characters.

        Methods:
            __str__(): Returns the username of the associated User as the string
            representation of the profile.
        """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_profiles"
    )
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

"""
Module: admin.py
Description: This module registers the models
- Letting,
- Address,
- and Profile
with the Django admin site.

Models:
    - Letting: A model representing a letting with a title and an associated
    address.
    - Address: A model representing a postal address.
    - Profile: A model representing a user's profile with a reference to the
    user and their favorite city.

Details:
    - The admin.site.register() function is used to make these models available
    in the Django admin interface.
"""

from django.contrib import admin

from lettings.models import Letting
from lettings.models import Address
from profiles.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
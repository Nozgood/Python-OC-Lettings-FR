"""
Module: urls.py
Description: This module defines the main URL patterns for the Django project.

URL Patterns:
    - '' : Maps to the index view, displaying the home page.
    - 'lettings/' : Includes the URL patterns from the 'lettings' application.
    - 'profiles/' : Includes the URL patterns from the 'profiles' application.
    - 'admin/' : Maps to the Django admin interface.

Details:
    - The include() function is used to reference the URL configurations of the
    'lettings' and 'profiles' applications.
    - The path() function is used to define the URL routes and their
    corresponding view functions or included URL configurations.
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]

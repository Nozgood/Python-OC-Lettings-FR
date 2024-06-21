"""
Module: urls.py
Description: This module defines the URL patterns for the 'profiles' application

URL Patterns:
    - '' : Maps to the index view, displaying the list of profiles.
    - '<str:username>/' : Maps to the profile view, displaying the details of a
    specific profile based on the username.

Namespaces:
    - app_name: The namespace for the 'profiles' application, set to "profiles".
"""

from django.urls import path
from profiles import views

app_name = "profiles"

urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]

"""
Module: urls.py
Description: This module defines the URL patterns for the 'lettings' application

URL Patterns:
    - '' : Maps to the index view, displaying the list of lettings.
    - '<int:letting_id>/' : Maps to the letting view, displaying the details of
    a specific letting based on its ID.

    Namespaces:
    - app_name: The namespace for the 'lettings' application, set to "lettings".
"""

from django.urls import path
from lettings import views

app_name = "lettings"

urlpatterns = [
    path('', views.index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]

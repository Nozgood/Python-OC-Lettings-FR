"""
Module: views.py
Description: This module contains the Django view functions for displaying lists
of user profiles and individual profile details.

Functions:
    - index(request): View function to display a list of all user profiles.
    - profile(request, username): View function to display the details of
    a specific user profile based on the username.

Details:
    - The index function retrieves all Profile objects and renders them in the
    'profiles/index.html' template.
    - The profile function retrieves a specific Profile object by the associated
    user's username and renders the profile details in the
    'profiles/profile.html' template.
"""

from profiles.models import Profile
from django.shortcuts import render


def index(request):
    """
        View function for displaying a list of user profiles.

        This view retrieves all Profile objects from the database and
        passes them to the 'profiles/index.html' template.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered HTML page displaying the list of
            user profiles.
        """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
        View function for displaying a single user's profile details.

        This view retrieves a Profile object based on the provided username
        and passes its details to the 'profiles/profile.html' template.

        Args:
            request (HttpRequest): The HTTP request object.
            username (str): The username of the User whose profile is to
            be retrieved.

        Returns:
            HttpResponse: The rendered HTML page displaying the details of the
            user's profile.
        """
    user_profile = Profile.objects.get(user__username=username)
    context = {'profile': user_profile}
    return render(request, 'profiles/profile.html', context)

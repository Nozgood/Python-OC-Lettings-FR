"""
Module: views.py
Description: This module contains the Django view functions for displaying
listings of lettings and the details of individual lettings.

Functions:
    - index(request): View function to display a list of all lettings.
    - letting(request, letting_id): View function to display the details of a
    specific letting based on its ID.

Details:
    - The index function retrieves all Letting objects and renders them in the
    'lettings/index.html' template.
    - The letting function retrieves a specific Letting object by its ID and
    renders its details in the 'lettings/letting.html' template.
"""

from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
        View function for displaying a list of lettings.

        This view retrieves all Letting objects from the database and passes
        them to the 'lettings/index.html' template.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered HTML page displaying the list of lettings
        """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
        View function for displaying a single letting's details.

        This view retrieves a Letting object based on the provided letting_id
        and passes its details to the 'lettings/letting.html' template.

        Args:
            request (HttpRequest): The HTTP request object.
            letting_id (int): The ID of the Letting object to be retrieved.

        Returns:
            HttpResponse: The rendered HTML page displaying the details
            of the letting.
        """
    lettings = Letting.objects.get(id=letting_id)
    context = {
        'title': lettings.title,
        'address': lettings.address,
    }
    return render(request, 'lettings/letting.html', context)

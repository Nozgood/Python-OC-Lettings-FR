"""
Module: views.py
Description: This module contains the Django view function for rendering the
home page of the application.

Functions:
    - index(request): View function to display the home page.

Details:
    - The index function renders the 'index.html' template.
"""


from django.shortcuts import render


def index(request):
    """
        View function for displaying the home page.

        This view renders the 'index.html' template.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered HTML page for the home page.
        """
    return render(request, 'index.html')

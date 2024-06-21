"""
Module: models.py
Description: This module contains the Django models for managing
addresses and lettings.

Classes:
    - Address: A model representing a postal address with fields for the
    street number, street name, city, state, ZIP code, and country ISO code.
    - Letting: A model representing a letting with a title and an
    associated address.

Details:
    - The Address model includes validation for each field to ensure proper
    data integrity.
    - The Letting model establishes a one-to-one relationship with the
    Address model, ensuring that each letting has a unique address.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
        A Django model representing a postal address.

        Attributes:
            number (int): The street number, validated to be a positive integer
            with a maximum value of 9999.
            street (str): The name of the street, with a maximum length of
            64 characters.
            city (str): The name of the city, with a maximum length of
            64 characters.
            state (str): The state abbreviation, which must be exactly
            2 characters long.
            zip_code (int): The ZIP code, validated to be a positive integer
            with a maximum value of 99999.
            country_iso_code (str): The ISO country code, which must be exactly
            3 characters long.

        Meta:
            verbose_name_plural (str): The plural name for the model in the
            admin interface, set to "Addresses".

        Methods:
            __str__(): Returns a string representation of the address,
            formatted as '{number} {street}'.
        """
    class Meta:
        verbose_name_plural = "Addresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)]
    )
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
        A Django model representing a letting, which includes a title and an
        associated address.

        Attributes:
            title (str): The title of the letting, with a maximum length of
            256 characters.
            address (Address): A one-to-one relationship with the Address model.
            When the associated Address is deleted, the Letting is also deleted.

        Methods:
            __str__(): Returns a string representation of the letting,
            which is its title.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

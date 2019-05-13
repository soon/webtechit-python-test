from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        db_index=True,
    )
    street_name = models.CharField(
        max_length=200,
        db_index=True,
        blank=True,
    )
    suburb = models.CharField(
        max_length=200,
        db_index=True,
        blank=True,
    )
    postcode = models.CharField(
        max_length=200,
        db_index=True,
        blank=True,
    )
    state = models.CharField(
        max_length=200,
        db_index=True,
        blank=True,
    )
    contact_name = models.CharField(
        max_length=200,
        db_index=True,
        blank=True,
    )
    email = models.EmailField(
        db_index=True,
    )
    phone_number = PhoneNumberField()

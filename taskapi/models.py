""" Models for taskapi app """
from __future__ import unicode_literals
from django.db import models


class Contact(models.Model):
    """
    The Contact class defines the main storage point for taskapi.
    Each Contact has four fields:
    __str__(self) - used to control if the name is displayed
    """
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    address = models.TextField()

    def __str__(self):
        return self.name

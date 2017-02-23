""" admin model register """
from django.contrib import admin
from .models import Contact

""" Register Contact model class """
admin.site.register(Contact)

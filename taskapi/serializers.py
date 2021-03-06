""" serializer form models """

from rest_framework import serializers
from taskapi.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    """ serializer class for models class """
    class Meta:
        """ Meta class for contact model fields """

        model = Contact
        fields = ('id', 'name', 'email', 'phone', 'address')

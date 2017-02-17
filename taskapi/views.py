from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from taskapi.serializers import ContactSerializer

@api_view(['GET'])
def contact_list(request):
    if request.method == 'GET':
        all_contact = Contact.objects.all()
        serializer = ContactSerializer(all_contact, many=True)
        return Response(serializer.data)

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from taskapi.models import Contact
from taskapi.serializers import ContactSerializer

@api_view(['GET', 'POST'])
def contact_list(request):
    if request.method == 'GET':
        all_contact = Contact.objects.all()
        serializer = ContactSerializer(all_contact, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

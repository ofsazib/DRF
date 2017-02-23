""" taskapi views """
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from taskapi.models import Contact
from taskapi.serializers import ContactSerializer

@api_view(['GET', 'POST'])
def contact_list(request):
    """press GET for all contact list, and
   { 
    "name": "",
    "email": "",
    "phone": "",
    "address": ""
    }
    \n and press POST button for insert new contact in the above format
    """
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

@api_view(['GET', 'PUT', 'DELETE'])
def contact_update_delete(request, contact_id):
    """
    press GET for view specific contact by id
    press PUT for update specific contact
    press DELETE for delete specific contact
    """
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

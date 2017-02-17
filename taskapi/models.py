from django.db import models

''' models class for taskapi app'''
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    address = models.TextField()

    def __str__(self):
        return self.name

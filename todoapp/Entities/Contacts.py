from django.db import models

# Create your models here.
class Contacts(models.Model):
    salutation = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    mobileNumber = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
    # created_at = models.DateTimeField('date published')
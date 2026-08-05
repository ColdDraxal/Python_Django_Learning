from django.db import models

# Create your models here.
class Person(models.Model):
    lastName = models.CharField(max_length=255, null=False)
    firstName = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    married = models.BooleanField(default="Unmarried")
    
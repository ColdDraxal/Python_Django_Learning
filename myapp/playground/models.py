from django.db import models

# Create your models here.
class Person(models.Model):
    lastName = models.CharField(max_length=255, null=False)
    firstName = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    married = models.BooleanField(default="Unmarried")

class Contact(models.Model):
    name =  models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    contact = models.CharField(max_length=255, null=False)
    subject = models.CharField(max_length=255, null=False)
    message = models.TextField(max_length=1000, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
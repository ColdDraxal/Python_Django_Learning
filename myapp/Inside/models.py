from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255, null=False)
    device = models.CharField(max_length=255, null=False)
    costly = models.BooleanField(default=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=255, null=False)
    playtime = models.DateTimeField('date_published')
    training = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1000, null=True,blank=True)
    coverImage = models.ImageField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return self.name
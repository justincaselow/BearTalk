from django.db import models


# Create your models here.
class Message(models.Model):
    timestamp = models.DateTimeField()
    message = models.CharField(max_length=500)
    bearId = models.CharField(max_length=50)

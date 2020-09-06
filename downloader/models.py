from django.db import models

# Create your models here.
class Activity(models.Model):
    link = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
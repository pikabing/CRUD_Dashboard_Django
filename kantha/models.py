from django.db import models
from django.urls import reverse

class Administrator(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    

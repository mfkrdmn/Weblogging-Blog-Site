import email
from django.db import models

# Create your models here.

class New_Blogger(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    reason = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


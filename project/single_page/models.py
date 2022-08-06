from django.db import models
from django.utils import timezone
from articles.models import *

class Comments(models.Model):
    commenter = models.CharField(max_length=50, blank=False)
    commented_post = models.IntegerField(default="1")
    commenterimg = models.ImageField(upload_to='commenterimg', default="profile.png", blank=True)
    date_commented = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=500, blank=False)
    commenter_email = models.CharField(max_length=50, blank=True, default="default_email")
    

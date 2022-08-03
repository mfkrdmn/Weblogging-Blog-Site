from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Articles(models.Model):
    user = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=80, blank=True)
    body =  RichTextField(max_length=231)
    body_long =  RichTextField(max_length=5000,default="long text here")
    picture = models.ImageField(upload_to='post_images', default="profile.png")
    # comment_number = models.IntegerField(default="0")

    def __str__(self) :
        return self.title

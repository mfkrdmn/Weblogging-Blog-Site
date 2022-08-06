from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Articles(models.Model):
    user = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=80, blank=True)
    body =  RichTextField(max_length=231)
    body_long =  RichTextField(max_length=5000,default="long text here")
    picture = models.ImageField(upload_to='post_images', default="profile.png")
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    def __str__(self) :
        return self.title


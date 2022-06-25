from django.db import models

# Create your models here.

# models.py
class Profile(models.Model):
    caption_name = models.CharField(max_length=50, blank=True, null=True)
    author_name = models.CharField(max_length=50,  blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/')



from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.apps import apps


class User(AbstractUser):
    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, default='profile_pic/profile_pic.png')
    status = models.BooleanField(default=False)
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)

    def __str__(self):
        return self.username


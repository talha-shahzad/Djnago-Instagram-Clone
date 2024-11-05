from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Story(models.Model):
    story_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_pic/')
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_stories')

    def __str__(self):
        return self.user.username + 's Story'
from django.db import models
from django.apps import apps
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    post_id=models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='post_pic/')
    caption = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts')
    def __str__(self):
        return self.caption

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pic/')

    def __str__(self):
        return f"Image for {self.post.caption}"
    
class Comment(models.Model):
    comment_id=models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
    
class Like(models.Model):
    like_id=models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.like_id
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     username=models.CharField(max_length=100)
#     bio = models.TextField()
#     profile_pic = models.ImageField(upload_to='profile_pic/', blank=True)
#     status = models.BooleanField(default=False)
#     follower=models.ManyToManyField('self',related_name='followers',symmetrical=False)
#     def __str__(self):
#         return self.name
#     def save(self, *args, **kwargs):
#         self.password = make_password(self.password)
#         super(User, self).save(*args, **kwargs)

class User(AbstractUser):
    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=10, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True)
    status = models.BooleanField(default=False)
    follower = models.ManyToManyField('self', related_name='followers', symmetrical=False)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id=models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='post_pic/')
    caption = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
    
class Like(models.Model):
    like_id=models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.like_id

class Story(models.Model):
    story_id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_pic/')
    date = models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='story_likes',blank=True)
    def __str__(self):
        return self.story_id
from django.contrib import admin

# Register your models here.
from .models import User,Post,PostImage,Comment,Like,Story

admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Story)


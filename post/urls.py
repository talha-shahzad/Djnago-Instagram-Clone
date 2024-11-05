from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.createpost, name='createpost'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.comment_post, name='comment_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('admin/', admin.site.urls),
]

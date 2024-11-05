from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.addstory, name='addstory'),
    path('latest/', views.latest_story, name='latest'),
    path('delete/<int:story_id>/', views.delete_story, name='delete_story'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

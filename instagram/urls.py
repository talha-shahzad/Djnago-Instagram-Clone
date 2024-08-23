from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/editProfile', views.editProfile, name='edit_profile'),
    path('follow/<str:username>/', views.toggle_follow, name='toggle_follow'),
    path('search', views.search, name='search'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
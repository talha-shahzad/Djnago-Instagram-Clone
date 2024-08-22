from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('',views.CustomLoginView.as_view(),name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('profile/editProfile',views.editProfile,name='edit_profile'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

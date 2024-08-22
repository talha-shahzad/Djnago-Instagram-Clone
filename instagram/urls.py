from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('',views.CustomLoginView.as_view(),name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('admin/', admin.site.urls),
]

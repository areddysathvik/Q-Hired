from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileUpdateView

urlpatterns = [
    path('',views.register,name='register'),
    path("profile/", ProfileUpdateView.as_view(), name='profile'),
    path("login/", LoginView.as_view(template_name='signin.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='signout.html'), name='logout'),
]

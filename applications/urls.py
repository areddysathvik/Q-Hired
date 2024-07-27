from django.contrib import admin
from django.urls import path, include
from .views import ApplicantCreateView
from . import views

urlpatterns = [
    path('',views.home_apply,name='home-applications' ),   
    path('<uuid:pk>/',ApplicantCreateView.as_view(), name='apply-for'),
]

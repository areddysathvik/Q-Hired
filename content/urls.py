from django.contrib import admin
from django.urls import path, include
from . import views 
from .views import PostedListView, PostedCreateView, PostedDetailView, download_resume

urlpatterns = [
    path('', views.PostedListView.as_view(),name='home'),
    path('job-create/', views.PostedCreateView.as_view(),name='job-create'),
    path('job/<uuid:pk>/', PostedDetailView.as_view(), name='job_detail'),
    path('download-resume/<int:pk>/', download_resume, name='download_resume'),
]

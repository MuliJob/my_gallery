from django.urls import path
from . import views

urlpatterns = [
  path('', views.home_page, name='home_page'),
  path('auth/register/', views.register, name='register'),
  path('auth/login/', views.login, name='login'),
  path('user-dashboard/', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('contact/', views.contact, name='contact'),
  path('photo-details/', views.photo_detail, name='photo_detail'),
  path('videos/', views.video, name='video'),
  path('video-detail', views.video_detail, name='video_detail'),
]
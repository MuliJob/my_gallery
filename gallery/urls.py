from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home_page, name='home_page'),
  path('signup/', views.authView, name='authView'),
  path("accounts/", include("django.contrib.auth.urls")),
  path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('user-dashboard/', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('contact/', views.contact, name='contact'),
  path('photo-details/<int:image_id>/', views.photo_detail, name='photo_detail'),
  path('videos/', views.video, name='video'),
  path('video-detail', views.video_detail, name='video_detail'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
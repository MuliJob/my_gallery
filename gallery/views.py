from django.shortcuts import render

# Create your views here.
def home_page(request):
  return render(request, 'home/index.html')

def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')

def photo_detail(request):
  return render(request, 'photo-detail.html')

def video(request):
  return render(request, 'videos.html')

def video_detail(request):
  return render(request, 'video-detail.html')
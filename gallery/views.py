from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  return render(request, 'index.html')

def authView(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('gallery:login')
  else:
    form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form' :form})


def home_page(request):
  return render(request, 'home/index.html')


def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')

@login_required
def photo_detail(request):
  return render(request, 'photo-detail.html')

@login_required
def video(request):
  return render(request, 'videos.html')

@login_required
def video_detail(request):
  return render(request, 'video-detail.html')
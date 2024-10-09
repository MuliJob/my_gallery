from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'login.html')  # Redirect back to the login page

        # Create a new user
        user = User.objects.create_user(email=email, full_name=full_name, password=password)
        user.save()
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('home')  # Redirect to the login page

    return render(request, 'auth/login.html')  # Render the registration form if GET request

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'auth/login.html')  # Render the login form if GET request


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
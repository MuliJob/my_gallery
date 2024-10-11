from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Image
from django.http import HttpResponse

@login_required
def home(request):
  images = Image.objects.all()
  return render(request, 'index.html', {'images': images})

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
def photo_detail(request, image_id):
  image = get_object_or_404(Image, id=image_id)

  related_images = Image.objects.filter(image_category=image.image_category).exclude(id=image.id)[:8]

  context = {
      'image': image,
      'related_images': related_images
  }
  return render(request, 'photo-detail.html', context)

def download_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    image_file = image.image.open()

    response = HttpResponse(image_file, content_type='image/jpeg')  # Adjust the content type as needed

    response['Content-Disposition'] = f'attachment; filename="{image.image_name}.jpg"'

    return response

@login_required
def video(request):
  return render(request, 'videos.html')

@login_required
def video_detail(request):
  return render(request, 'video-detail.html')
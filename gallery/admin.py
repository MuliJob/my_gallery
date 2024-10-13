from django.contrib import admin
from .models import Location, Category, Image, Video, VideoCategory, VideoLocation

# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(VideoCategory)
admin.site.register(VideoLocation)
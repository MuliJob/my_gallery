from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def save_location(self):
        self.save()

    def update_location(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def save_category(self):
        self.save()

    def update_category(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=255)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, image_name=None, image_description=None, image_location=None, image_category=None):
        if image_name:
            self.image_name = image_name
        if image_description:
            self.image_description = image_description
        if image_location:
            self.image_location = image_location
        if image_category:
            self.image_category = image_category
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def search_image(cls, category):
        return cls.objects.filter(image_category__name__icontains=category)

    @classmethod
    def filter_by_location(cls, location):
        return cls.objects.filter(image_location__name__icontains=location)

    def __str__(self):
        return self.image_name
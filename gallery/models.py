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

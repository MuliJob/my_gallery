from django.test import TestCase
from .models import Location, Category

class LocationModelTest(TestCase):

    def setUp(self):
        self.location = Location.objects.create(name="Park", description="A beautiful park.")

    def test_create_location(self):
        self.assertEqual(self.location.name, "Park")
        self.assertEqual(self.location.description, "A beautiful park.")

    def test_update_location(self):
        self.location.update_location(name="City Park", description="A large city park.")
        self.location.refresh_from_db()
        self.assertEqual(self.location.name, "City Park")
        self.assertEqual(self.location.description, "A large city park.")

    def test_delete_location(self):
        self.location.delete_location()
        with self.assertRaises(Location.DoesNotExist):
            Location.objects.get(id=self.location.id)

    def test_str_method(self):
        self.assertEqual(str(self.location), "Park")

    def test_save_location(self):
        new_location = Location(name="Beach", description="A sunny beach.")
        new_location.save_location()
        self.assertEqual(Location.objects.count(), 2)

    def test_update_location_with_partial_data(self):
        self.location.update_location(description="A park in the city.")
        self.location.refresh_from_db()
        self.assertEqual(self.location.description, "A park in the city.")
        self.assertEqual(self.location.name, "Park")

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Morning", description="Morning pictures.")

    def test_create_category(self):
        self.assertEqual(self.category.name, "Morning")
        self.assertEqual(self.category.description, "Morning pictures.")

    def test_update_category(self):
        self.category.update_category(name="Plants", description="Plants Images.")
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "Plants")
        self.assertEqual(self.category.description, "Plants Images.")

    def test_delete_category(self):
        self.category.delete_category()
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=self.category.id)

    def test_str_method(self):
        self.assertEqual(str(self.category), "Morning")

    def test_save_location(self):
        new_category = Category(name="Clocks", description="Clocks in my gallery.")
        new_category.save_category()
        self.assertEqual(Category.objects.count(), 2)

    def test_update_category_with_partial_data(self):
        self.category.update_category(description="Morning pictures")
        self.category.refresh_from_db()
        self.assertEqual(self.category.description, "Morning pictures")
        self.assertEqual(self.category.name, "Morning")
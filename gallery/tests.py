from django.test import TestCase
from .models import Location, Category, Image

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

class ImageModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name="Test Location", description="Test Description")
        self.category = Category.objects.create(name="Test Category", description="Test Category Description")
        self.image = Image.objects.create(
            image_name="Test Image",
            image_description="Test Image Description",
            image_location=self.location,
            image_category=self.category
        )

    def test_save_image(self):
        self.image.save_image()
        self.assertIsNotNone(Image.objects.get(id=self.image.id))

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        with self.assertRaises(Image.DoesNotExist):
            Image.objects.get(id=self.image.id)

    def test_update_image(self):
        new_name = "Updated Image Name"
        new_description = "Updated Image Description"
        self.image.update_image(image_name=new_name, image_description=new_description)
        self.image.refresh_from_db()
        self.assertEqual(self.image.image_name, new_name)
        self.assertEqual(self.image.image_description, new_description)

    def test_get_image_by_id(self):
        retrieved_image = Image.get_image_by_id(self.image.id)
        self.assertEqual(retrieved_image, self.image)

    def test_get_image_by_id_non_existent(self):
        retrieved_image = Image.get_image_by_id(99999)  # ID that doesn't exist
        self.assertIsNone(retrieved_image)

    def test_search_image(self):
        images = Image.search_image("Test Category")
        self.assertIn(self.image, images)

    def test_filter_by_location(self):
        images = Image.filter_by_location("Test Location")
        self.assertIn(self.image, images)

    def test_str_method(self):
        self.assertEqual(str(self.image), "Test Image")
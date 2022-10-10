from apps.product.models import Category
from django.test import TestCase


class CategoryModelTestCase(TestCase):
    
    def setUp(self):
        Category.objects.create(
            category_name = 'Informática'
        )

    def test_category_return_str(self):
        category = Category.objects.get(category_name='Informática')
        self.assertEquals(category.__str__(), 'Informática')

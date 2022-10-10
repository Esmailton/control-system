from apps.product.models import Category
from django.test import TestCase
from django.urls import reverse


class CategoryViewTestCase(TestCase):
    
    def test_category_status_code_200(self):
        response = self.client.get(reverse('category_view_add'))
        self.assertAlmostEquals(response.status_code, 200)


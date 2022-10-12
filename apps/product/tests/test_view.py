from django.test import TestCase
from django.urls import reverse


class CategoryViewTestCase(TestCase):
    
    def test_category_status_code_302(self):
        response = self.client.get(reverse('category_view_add'))
        self.assertEqual(response.status_code, 302)

    def test_product_status_code_302(self):
        response = self.client.get(reverse('product_view_add'))
        self.assertEquals(response.status_code, 302)

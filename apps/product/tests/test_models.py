from apps.product.models import Category, Product
from django.test import TestCase


class CategoryModelTestCase(TestCase):
    
    def setUp(self):
        Category.objects.create(
            category_name = 'Informática'
        )

    def test_category_return_str(self):
        category = Category.objects.get(category_name='Informática')
        self.assertEquals(category.__str__(), 'Informática')


class ProductModelTestCase(TestCase):
    
    def setUp(self):
        Category.objects.create(
            category_name = 'Informática'
        )
        category = Category.objects.get(category_name='Informática')
        Product.objects.create(
            product_name = 'Mouse',
            product_price = 100.00,
            product_category = category,
            product_photo = None,
            product_description = 'Mouse sem Fio',
            product_bar_code = '1323232320123'
        )

    def test_product_return_str(self):
        product = Product.objects.get(product_name='Mouse')
        self.assertEqual(product.__str__(), 'Mouse')

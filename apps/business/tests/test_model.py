from django.test import TestCase
from .business_test_base import FakeDataFactory
from parameterized import parameterized
from django.core.exceptions import ValidationError


class CategoryModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.category = self.factory.create_category()
    
    @parameterized.expand([
            ('name', 100)
        ])

    def test_field_category_max_length(self, field, max_length):
        setattr(self.category, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_category_representation(self):
        self.assertEqual(
            self.category.name,
            str(self.category)
        )

    def test_category_get_absolute_url(self):
        self.assertEqual(f'/category/detail/{self.category.id}/', self.category.get_absolute_url())


class MeasureTypeModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.measure_type = self.factory.create_measure_type()

    @parameterized.expand([
        ('name', 100),
        ('measure_type', 100),
        ('acronym', 4),
    ])

    def test_fields_measure_type_max_length(self, field, max_length):
        setattr(self.measure_type, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.measure_type.full_clean()
    
    def test_measure_type_representation(self):
        self.assertEqual(
            self.measure_type.name,
            str(self.measure_type)
        )

    def test_measure_type_get_absolute_url(self):
        self.assertEqual(
            f'/measure_type/detail/{self.measure_type.id}/',
            self.measure_type.get_absolute_url()
        )


class ProductModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.product = self.factory.create_product()

    @parameterized.expand([
        ('name', 100)
    ])

    def test_fields_product_max_length(self, field, max_length):
        setattr(self.product, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.product.full_clean()
    
    def test_product_representation(self):
        self.assertEqual(
            self.product.name,
            str(self.product)
        )

    def test_product_get_absolute_url(self):
        self.assertEqual(
            f'/product/detail/{self.product.id}/',
            self.product.get_absolute_url()
        )

class ServiceModelTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.service = self.factory.create_service()

    @parameterized.expand([
        ('name', 100)
    ])

    def test_fields_service_max_length(self, field, max_length):
        setattr(self.service, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.service.full_clean()
    
    def test_service_representation(self):
        self.assertEqual(
            self.service.name,
            str(self.service)
        )

    def test_service_get_absolute_url(self):
        self.assertEqual(
            f'/service/detail/{self.service.id}/',
            self.service.get_absolute_url()
        )

class inventoryModelTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.inventory = self.factory.create_inventory()

    def test_inventory_representation(self):
        self.assertEqual(
            str(self.inventory.quantity),
            str(self.inventory)
        )
    def test_inventory_absolute_url(self):
        self.assertEqual(self.inventory.get_absolute_url(), f'/inventory/detail/{self.inventory.id}/')
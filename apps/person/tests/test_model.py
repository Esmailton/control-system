from django.test import TestCase
from django.core.exceptions import ValidationError
from .person_base_test import FakeDataFactory
from parameterized import parameterized

''
class PersonModelTest(TestCase):
    
    def setUp(self):
        self.factory = FakeDataFactory()
        self.person = self.factory.create_person()

    @parameterized.expand([
            ('name', 100),    
            ('document', 14),
        ])
    
    def test_person_fields_max_length(self, field,max_length):
        setattr(self.person, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.person.full_clean()

    def test_person_representation(self):
        self.assertEqual(
            str(self.person),
            self.person.name
        )
    
    def test_person_get_absolute_url(self):
        self.assertEqual(f'/person/detail/{self.person.id}/', self.person.get_absolute_url())


class PhoneModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.phone = self.factory.create_phone()
    
    @parameterized.expand([
        ('phone', 14),
        ('type', 2),
    ])
    def test_phone_field_max_length(self, field, max_length):
        setattr(self.phone, field, '1' * (max_length + 10))
        with self.assertRaises(ValidationError):
            self.phone.full_clean()

    def test_phone_representation(self):
        self.assertEqual(
            str(self.phone),
            self.phone.phone
        )

    def test_phone_get_absolute_url(self):
        self.assertEqual(f'/phone/detail/{self.phone.id}/', self.phone.get_absolute_url())


class EmailModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.email = self.factory.create_email()
    
    @parameterized.expand([
        ('type', 2),
    ])
    def test_email_field_max_length(self, field, max_length):
        setattr(self.email, field, '1' * (max_length + 10))
        with self.assertRaises(ValidationError):
            self.email.full_clean()

    def test_email_representation(self):
        self.assertEqual(
            str(self.email),
            self.email.email
        )

    def test_email_get_absolute_url(self):
        self.assertEqual(f'/email/detail/{self.email.id}/', self.email.get_absolute_url())
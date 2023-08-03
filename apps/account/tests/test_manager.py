from django.test import TestCase
from faker import Faker
from django.contrib.auth import get_user_model


class UserManagerTestes(TestCase):
    User = get_user_model()

    def test_create_user(self):
        username = str(Faker().first_name()).lower()
        password = 'TestPass123*'

        user = self.User.objects.create_user(username, password)
        self.assertEqual(user.username, username)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        username = str(Faker().first_name()).lower()
        password = 'TestPass123*'
        admin_user = self.User.objects.create_superuser(username=username, password=password)
        self.assertEqual(admin_user.username, username)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
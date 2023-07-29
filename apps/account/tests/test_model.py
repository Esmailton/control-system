from django.test import TestCase
from .account_base_test import FakeDataFactory
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError, DataError

class AccountModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.user = self.factory.create_user()

    def test_representation(self):
        self.assertEqual(str(self.user), self.user.username)

    def test_duplicate_user_test(self):
        with self.assertRaises(IntegrityError):
            get_user_model().objects.create(
                username=self.user.username,
                password='--FakePassword*'
            )

    def test_null_username(self):
        with self.assertRaises(IntegrityError):
            get_user_model().objects.create(
                username=None,
                password='--FakePassword*'
            )

    def test_blank_password(self):
        with self.assertRaises(IntegrityError):
            user = get_user_model().objects.create(
                    username='newuser',
                    password=None
            )
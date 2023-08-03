from unittest.mock import patch
from django.test import TestCase

from apps.account.models import UserCustom
from ..form import UserCreationForm
from datetime import date
from faker import Faker


class UserCreationFormTest(TestCase):

    username = str(Faker().first_name()).lower()
    password = 'TestPass123*'

    def test_form_create_account_valid_data(self):
        form_data = {
            'username': self.username,
            'password': self.password,
            'password2': self.password,
            'date_joined': date.today()
        }
        form = UserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_password_confirmation(self):
        form_data = {
            'username': self.username,
            'password': self.password+'1',
            'password2': self.password,
            'date_joined': date.today()
        }
        form = UserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_username(self):
        form_data = {
            'username': None,
            'password': self.password,
            'password2': self.password,
            'date_joined': date.today()
        }
        form = UserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_save(self):
        form_data = {
            'username': self.username,
            'password': self.password,
            'password2': self.password,
            'date_joined': date.today()
        }

        form = UserCreationForm(data=form_data)
        user = form.save()
        self.assertEqual(user.username, self.username)
        self.assertTrue(user.check_password(self.password))
        saved_user = UserCustom.objects.get(username=self.username)
        self.assertEqual(saved_user, user)


    def test_save_with_commit_true(self):
        form_data = {
            'username': self.username,
            'password': self.password,
            'password2': self.password,
        }

        form = UserCreationForm(data=form_data)
        with patch.object(UserCustom, 'save') as mock_save:
            form.save()
        mock_save.assert_called_once()

    def test_save_with_commit_false(self):
        form_data = {
            'username': self.username,
            'password': self.password,
            'password2': self.password,
        }
        form = UserCreationForm(data=form_data)
        with patch.object(UserCustom, 'save') as mock_save:
            form.save(commit=False)
        mock_save.assert_not_called()
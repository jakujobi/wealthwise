import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from users.forms import UserRegistrationForm, UserProfileForm

User = get_user_model()

# Pytest style tests
@pytest.mark.django_db
class TestUserRegistrationForm:
    def test_valid_registration_form(self):
        form_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        form = UserRegistrationForm(data=form_data)
        assert form.is_valid()

    def test_password_mismatch(self):
        form_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'testpass123',
            'password2': 'differentpass'
        }
        form = UserRegistrationForm(data=form_data)
        assert not form.is_valid()
        assert 'password2' in form.errors

# Django TestCase style tests
class UserProfileFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='formtest',
            email='form@example.com',
            password='testpass123'
        )

    def test_valid_profile_form(self):
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'bio': 'Test bio'
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_profile_form(self):
        form = UserProfileForm(data={})
        self.assertTrue(form.is_valid())  # Profile form should be valid with empty data 
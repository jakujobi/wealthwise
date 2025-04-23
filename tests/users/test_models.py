import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import UserProfile

User = get_user_model()

# Pytest style tests
@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        assert user.username == 'testuser'
        assert user.email == 'test@example.com'
        assert user.check_password('testpass123')
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_superuser(self):
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        assert admin.is_staff
        assert admin.is_superuser

# Django TestCase style tests
class UserProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='profiletest',
            email='profile@example.com',
            password='testpass123'
        )
        self.profile = UserProfile.objects.create(user=self.user)

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertIsNotNone(self.profile.created_at)
        self.assertIsNotNone(self.profile.updated_at)

    def test_profile_str_representation(self):
        expected_str = f"{self.user.username}'s profile"
        self.assertEqual(str(self.profile), expected_str) 
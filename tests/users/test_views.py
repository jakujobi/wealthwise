import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import UserProfile

User = get_user_model()

# Pytest style tests
@pytest.mark.django_db
class TestUserViews:
    def test_user_registration(self, client):
        url = reverse('user-register')
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        response = client.post(url, data)
        assert response.status_code == 302  # Redirect after successful registration
        assert User.objects.filter(username='newuser').exists()

    def test_user_login(self, client, test_user):
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = client.post(url, data)
        assert response.status_code == 302  # Redirect after successful login

# Django TestCase style tests
class UserViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='viewtest',
            email='view@example.com',
            password='testpass123'
        )
        self.profile = UserProfile.objects.create(user=self.user)

    def test_profile_view(self):
        self.client.login(username='viewtest', password='testpass123')
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_profile_update(self):
        self.client.login(username='viewtest', password='testpass123')
        url = reverse('profile-update')
        data = {
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User') 
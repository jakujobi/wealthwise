import pytest
from django.test import TestCase, Client
from django.urls import reverse
from tests.users.factories import UserFactory

# Pytest style tests
@pytest.mark.django_db
class TestLearningViews:
    def test_learning_home_view(self, client, test_user):
        client.login(username='testuser', password='testpass123')
        url = reverse('learning-home')
        response = client.get(url)
        assert response.status_code == 200
        assert 'learning/home.html' in [t.name for t in response.templates]

# Django TestCase style tests
class LearningViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.client.login(username=self.user.username, password='testpass123')

    def test_learning_resources_access(self):
        url = reverse('learning-resources')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning/resources.html') 
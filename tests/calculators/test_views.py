import pytest
from django.test import TestCase, Client
from django.urls import reverse
from tests.calculators.factories import FinancialToolUsageFactory
from tests.users.factories import UserFactory

# Pytest style tests
@pytest.mark.django_db
class TestCalculatorViews:
    def test_budget_calculator_view(self, client, test_user):
        client.login(username='testuser', password='testpass123')
        url = reverse('budget-calculator')
        response = client.get(url)
        assert response.status_code == 200
        assert 'budget' in response.context

    def test_compound_interest_calculator_view(self, client, test_user):
        client.login(username='testuser', password='testpass123')
        url = reverse('compound-interest-calculator')
        response = client.get(url)
        assert response.status_code == 200
        assert 'compound_interest' in response.context

    def test_retirement_calculator_view(self, client, test_user):
        client.login(username='testuser', password='testpass123')
        url = reverse('retirement-calculator')
        response = client.get(url)
        assert response.status_code == 200
        assert 'retirement' in response.context

# Django TestCase style tests
class CalculatorViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.client.login(username=self.user.username, password='testpass123')

    def test_budget_calculator_post(self):
        url = reverse('budget-calculator')
        data = {
            'income': 5000,
            'expenses': {
                'housing': 1500,
                'food': 500,
                'transportation': 300,
                'utilities': 200,
                'entertainment': 300
            }
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json())

    def test_compound_interest_calculator_post(self):
        url = reverse('compound-interest-calculator')
        data = {
            'principal': 10000,
            'rate': 0.05,
            'years': 10,
            'compound_frequency': 12
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json()) 
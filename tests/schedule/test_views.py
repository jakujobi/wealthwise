import pytest
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime, timedelta
from tests.schedule.factories import ConsultationFactory, EventFactory
from tests.users.factories import UserFactory

# Pytest style tests
@pytest.mark.django_db
class TestScheduleViews:
    def test_consultation_list_view(self, client, test_user):
        client.login(username='testuser', password='testpass123')
        ConsultationFactory.create_batch(3, client_id=test_user.profile)
        url = reverse('consultation-list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.context['consultations']) == 3

    def test_event_list_view(self, client, test_user):
        client.login(username='testuser', password='testpass123')
        EventFactory.create_batch(3, user_id=test_user.profile)
        url = reverse('event-list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.context['events']) == 3

# Django TestCase style tests
class ScheduleViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.client.login(username=self.user.username, password='testpass123')

    def test_create_consultation(self):
        url = reverse('consultation-create')
        data = {
            'advisor_id': UserFactory().id,
            'scheduled_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'scheduled'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation

    def test_create_event(self):
        url = reverse('event-create')
        data = {
            'title': 'Test Event',
            'description': 'Test Description',
            'event_start_timestamp': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'event_end_timestamp': (datetime.now() + timedelta(days=1, hours=2)).strftime('%Y-%m-%d %H:%M:%S'),
            'location': 'Test Location'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation

    def test_update_consultation(self):
        consultation = ConsultationFactory(client_id=self.user.profile)
        url = reverse('consultation-update', kwargs={'pk': consultation.consultation_id})
        data = {
            'status': 'completed',
            'client_rating': 5,
            'session_notes': 'Great session!'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful update

    def test_delete_event(self):
        event = EventFactory(user_id=self.user.profile)
        url = reverse('event-delete', kwargs={'pk': event.event_id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion 
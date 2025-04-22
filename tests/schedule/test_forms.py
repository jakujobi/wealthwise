import pytest
from django.test import TestCase
from datetime import datetime, timedelta
from schedule.forms import ConsultationForm, EventForm
from tests.users.factories import UserFactory

# Pytest style tests
@pytest.mark.django_db
class TestScheduleForms:
    def test_valid_consultation_form(self):
        advisor = UserFactory()
        form_data = {
            'advisor_id': advisor.id,
            'scheduled_date': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'scheduled'
        }
        form = ConsultationForm(data=form_data)
        assert form.is_valid()

    def test_invalid_consultation_form(self):
        form_data = {
            'advisor_id': '',  # Required field
            'scheduled_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Past date
            'status': 'invalid_status'  # Invalid choice
        }
        form = ConsultationForm(data=form_data)
        assert not form.is_valid()
        assert len(form.errors) >= 2

# Django TestCase style tests
class EventFormTests(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_valid_event_form(self):
        form_data = {
            'title': 'Test Event',
            'description': 'Test Description',
            'event_start_timestamp': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'event_end_timestamp': (datetime.now() + timedelta(days=1, hours=2)).strftime('%Y-%m-%d %H:%M:%S'),
            'location': 'Test Location'
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_event_dates(self):
        form_data = {
            'title': 'Test Event',
            'description': 'Test Description',
            'event_start_timestamp': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'event_end_timestamp': (datetime.now() + timedelta(days=1, hours=-1)).strftime('%Y-%m-%d %H:%M:%S'),
            'location': 'Test Location'
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('event_end_timestamp', form.errors)

    def test_missing_required_fields(self):
        form_data = {
            'description': 'Test Description',
            'location': 'Test Location'
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('event_start_timestamp', form.errors)
        self.assertIn('event_end_timestamp', form.errors) 
import pytest
from django.test import TestCase
from datetime import datetime, timedelta
from schedule.models import Consultation, Event
from tests.schedule.factories import ConsultationFactory, EventFactory

# Pytest style tests
@pytest.mark.django_db
class TestConsultation:
    def test_consultation_creation(self):
        consultation = ConsultationFactory()
        assert consultation.consultation_id is not None
        assert consultation.client_id is not None
        assert consultation.advisor_id is not None
        assert consultation.scheduled_date is not None
        assert consultation.status in ['scheduled', 'completed', 'cancelled']

    def test_consultation_str_representation(self):
        consultation = ConsultationFactory()
        expected_str = f"Consultation {consultation.consultation_id} - {consultation.scheduled_date}"
        assert str(consultation) == expected_str

@pytest.mark.django_db
class TestEvent:
    def test_event_creation(self):
        event = EventFactory()
        assert event.event_id is not None
        assert event.user_id is not None
        assert event.title is not None
        assert event.event_start_timestamp is not None
        assert event.event_end_timestamp is not None
        assert event.event_end_timestamp > event.event_start_timestamp

    def test_event_str_representation(self):
        event = EventFactory()
        assert str(event) == str(event.event_id)

# Django TestCase style tests
class ConsultationTests(TestCase):
    def setUp(self):
        self.consultation = ConsultationFactory()

    def test_consultation_rating_range(self):
        self.consultation.client_rating = 6
        with self.assertRaises(Exception):
            self.consultation.full_clean()

        self.consultation.client_rating = 0
        with self.assertRaises(Exception):
            self.consultation.full_clean()

class EventTests(TestCase):
    def setUp(self):
        self.event = EventFactory()

    def test_event_dates_validation(self):
        self.event.event_end_timestamp = self.event.event_start_timestamp - timedelta(hours=1)
        with self.assertRaises(Exception):
            self.event.full_clean()

    def test_event_title_max_length(self):
        self.event.title = 'a' * 101  # Title max_length is 100
        with self.assertRaises(Exception):
            self.event.full_clean() 
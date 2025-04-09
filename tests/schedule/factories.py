import factory
from datetime import datetime, timedelta
from schedule.models import Consultation, Event
from tests.users.factories import UserProfileFactory

class ConsultationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Consultation

    client_id = factory.SubFactory(UserProfileFactory)
    advisor_id = factory.SubFactory(UserProfileFactory)
    scheduled_date = factory.Faker('date_time_this_month')
    status = factory.Faker('random_element', elements=['scheduled', 'completed', 'cancelled'])
    client_rating = factory.Faker('random_int', min=1, max=5)
    session_notes = factory.Faker('text')

class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    user_id = factory.SubFactory(UserProfileFactory)
    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('paragraph')
    event_start_timestamp = factory.Faker('date_time_this_month')
    event_end_timestamp = factory.LazyAttribute(
        lambda obj: obj.event_start_timestamp + timedelta(hours=2)
    )
    location = factory.Faker('address') 
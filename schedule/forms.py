from django.forms import ModelForm
from .models import *

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_start_timestamp', 'event_end_timestamp', 'location']

class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ['scheduled_date', 'status', 'client_rating', 'session_notes']
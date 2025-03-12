from django.forms import ModelForm
from .models import *

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time', 'location', 'advisor_id']

class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ['title', 'description', 'start_time', 'end_time', 'location', 'advisor_id', 'client_id']
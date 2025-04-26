from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_start_timestamp', 'event_end_timestamp', 'location']

class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ['scheduled_date', 'status', 'client_rating', 'session_notes']

class AdvisorAvailabilityForm(ModelForm):
    class Meta:
        model = AdvisorAvailability
        fields = ['blockedDateTime']  # Only include fields that exist in the model

class TimeSlotForm(ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['day_of_week', 'start_time', 'end_time']  # Fields for individual time slots

class ConsultationBookingForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ['advisor_id', 'scheduled_date', 'session_notes']

    def clean(self):
        cleaned_data = super().clean()
        advisor = cleaned_data.get('advisor_id')
        scheduled_date = cleaned_data.get('scheduled_date')

        # Ensure scheduled_date is in the future
        if scheduled_date and scheduled_date <= now():
            raise ValidationError("The scheduled date must be in the future.")

        # Check if the scheduled_date conflicts with the advisor's blocked dates
        if advisor:
            availability = AdvisorAvailability.objects.filter(advisor=advisor).first()
            if availability and availability.blockedDateTime:
                for blocked in availability.blockedDateTime:
                    blocked_start = blocked.get('start_time')
                    blocked_end = blocked.get('end_time')
                    if blocked_start and blocked_end and blocked_start <= scheduled_date <= blocked_end:
                        raise ValidationError("The selected time conflicts with the advisor's blocked schedule.")

        return cleaned_data
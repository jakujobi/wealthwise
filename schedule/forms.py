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
        fields = ['advisor_id', 'scheduled_date', 'session_notes', 'time_slot']

    def clean(self):
        cleaned_data = super().clean()
        advisor = cleaned_data.get('advisor_id')
        scheduled_date = cleaned_data.get('scheduled_date')
        time_slot = cleaned_data.get('time_slot')

        # Ensure scheduled_date is in the future
        if scheduled_date and scheduled_date <= now():
            raise ValidationError("The scheduled date must be in the future.")

        # Validate time slot availability
        if time_slot:
            if time_slot.availability.advisor != advisor:
                raise ValidationError("The selected time slot does not belong to the chosen advisor.")
            overlapping_consultations = Consultation.objects.filter(
                time_slot=time_slot,
                scheduled_date__date=scheduled_date.date()
            )
            if overlapping_consultations.exists():
                raise ValidationError("The selected time slot is already booked.")

        return cleaned_data
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from django.utils import timezone

# Consultation
class Consultation(models.Model):
    consultation_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey('users.Profile', related_name='client', on_delete=models.CASCADE)
    advisor_id = models.ForeignKey('users.Advisor', on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    status = models.CharField(max_length=20, blank=True, null=True)
    client_rating = models.IntegerField(blank=True, null=True)
    session_notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Consultation {self.consultation_id} - {self.scheduled_date}"

# Event
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    event_start_timestamp = models.DateTimeField()
    event_end_timestamp = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return str(self.event_id)

class eventRegistration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    registration_date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return str(self.event_id)

class AdvisorAvailability(models.Model):
    advisor = models.ForeignKey('users.Advisor', on_delete=models.CASCADE)
    blockedDateTime = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return f"{self.advisor.user.username} - {self.time_slots.count()} time slots, {len(self.blockedDateTime or [])} blocked slots"

class TimeSlot(models.Model):
    availability = models.ForeignKey(AdvisorAvailability, related_name='time_slots', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=[
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day_of_week}: {self.start_time} - {self.end_time}"
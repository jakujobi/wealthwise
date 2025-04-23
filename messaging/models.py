from django.db import models
from django.conf import settings

# Create your models here.

class Conversation(models.Model):
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='conversations'
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        related_name='messages',
        on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='sent_messages',
        on_delete=models.CASCADE
    )
    body = models.TextField(blank=True)
    attachments = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='read_messages',
        blank=True
    )

class NotificationSetting(models.Model):
    EVENT_TYPES = [
        ('appointment_reminder', 'Appointment Reminder'),
        ('new_message', 'New Message'),
        ('renewal', 'Renewal'),
        ('upcoming_event', 'Upcoming Event'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notification_settings'
    )
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    email = models.BooleanField(default=True)
    sms = models.BooleanField(default=False)
    in_app = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'event_type')

class ArchivedConversation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='archived_conversations'
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='archived_by'
    )
    archived_at = models.DateTimeField(auto_now_add=True)

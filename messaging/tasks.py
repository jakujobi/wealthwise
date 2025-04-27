from celery import shared_task
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
from .models import Message, NotificationSetting

@shared_task
def send_notifications_for_message(message_id):
    msg = Message.objects.get(id=message_id)
    conv = msg.conversation
    sender = msg.sender
    body = msg.body
    # Notify other participants
    for user in conv.participants.exclude(id=sender.id):
        ns = NotificationSetting.objects.filter(user=user, event_type='new_message').first()
        if not ns:
            continue
        # Email via SendGrid
        if ns.email and settings.SENDGRID_API_KEY:
            email_msg = Mail(
                from_email=settings.DEFAULT_FROM_EMAIL,
                to_emails=user.email,
                subject=f"New message from {sender.username}",
                html_content=f"<p>{body}</p>"
            )
            try:
                SendGridAPIClient(settings.SENDGRID_API_KEY).send(email_msg)
            except Exception as e:
                print(f"SendGrid error: {e}")
        # SMS via Twilio
        if ns.sms and settings.TWILIO_ACCOUNT_SID:
            try:
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                client.messages.create(
                    body=f"New message from {sender.username}: {body}",
                    from_=settings.TWILIO_FROM_NUMBER,
                    to=user.profile.phone_number
                )
            except Exception as e:
                print(f"Twilio error: {e}")

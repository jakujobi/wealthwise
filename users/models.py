from django.db import models
from django.contrib.postgres.fields import JSONField

# Profile
class Profile(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    user_role = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    financial_goals = JSONField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    privacy_settings = JSONField(blank=True, null=True)

# AdvisorProfile
class Advisor(models.Model):
    advisor_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(users.Profile, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    certifications = JSONField(blank=True, null=True)
    specialties = JSONField(blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)

# Subsciption
class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(users.Profile, on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=10, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    auto_renew = models.BooleanField(default=False)

# PaymentHistory
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(users.Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)

# Messages
class Messaging(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey(users.Profile, related_name='sender', on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(users.Profile, related_name='receiver', on_delete=models.CASCADE)
    message_content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)

# Notification
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(users.Profile, on_delete=models.CASCADE)
    content = models.TextField()
    notification_type = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
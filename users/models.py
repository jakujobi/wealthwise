from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    privacy_settings = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        try:
            this = Profile.objects.get(id=self.id) # type: ignore
            if this.profile_picture != self.profile_picture:
                this.profile_picture.delete(save=False)
        except Profile.DoesNotExist:
            pass
        # Update related User model if needed
        if hasattr(self, 'user'):
            self.user.save()
        super(Profile, self).save(*args, **kwargs)

# AdvisorProfile
class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='advisor')
    bio = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    specialties = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.0'))
    
    def __str__(self):
        return f"Advisor: {self.user.username}"

# Subsciption
class Subscription(models.Model):
    user_id = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=10, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    auto_renew = models.BooleanField(default=False)

# PaymentHistory
class Payment(models.Model):
    user_id = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)

# Messages
class Messaging(models.Model):
    sender_id = models.ForeignKey('users.Profile', related_name='sender', on_delete=models.CASCADE)
    receiver_id = models.ForeignKey('users.Profile', related_name='receiver', on_delete=models.CASCADE)
    message_content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)

# Notification
class Notification(models.Model):
    user_id = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    content = models.TextField()
    notification_type = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
from django.contrib import admin
from .models import Profile, Advisor, Subscription, Payment, Messaging, Notification

admin.site.register(Profile)
admin.site.register(Advisor)
admin.site.register(Subscription)
admin.site.register(Payment)
admin.site.register(Messaging)
admin.site.register(Notification)

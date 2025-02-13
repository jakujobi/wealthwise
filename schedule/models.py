from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    isPublished = models.BooleanField(default=False)
    timezone = models.CharField(max_length=200, default='UTC-6') # default to central time

    def __str__(self):
        return self.title

# Create your models here.

# Consultation

# Event
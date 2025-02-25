from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event
import datetime
import math

"""  
! ALL TIME WILL CONVERT TO UTC-6 TIME FORMAT
! CONVERT TO THE USER LOCAL TIME ZONE IF NEEDED
"""

# Create your views here.
@login_required
# myEvents
def myEvents(request):
     today = datetime.datetime.now()
     year_now = today.year
     month_now = today.month
     day_now = today.day
     local_tzone = today.astimezone().tzinfo

     # Check if the current user is an advisor
     isAllowToModify = hasattr(request.user.profile, 'advisor') or request.user.is_staff or request.user.is_superuser

     # Get all events
     # events = Event.objects.all()
     events = Event.objects.filter(event_start_date__gt=datetime.datetime.now())

     return render(request, 'myEvents.html', {
         'events': events,
         'isAllowToModify': isAllowToModify
     })

# Event Register
@login_required
def eventRegister(request):
     today = datetime.datetime.now()
     year_now = today.year
     month_now = today.month
     day_now = today.day
     local_tzone = today.astimezone().tzinfo

     # Check if the current user is an advisor
     isAllowToModify = hasattr(request.user.profile, 'advisor') or request.user.is_staff or request.user.is_superuser

     errors = Event.check()
     if errors:
          return render(request, 'eventRegister.html', {'errors': errors})
     
     if request.method == 'GET':
        # Get all events in the future from the current time
        events = Event.objects.filter(event_start_date__gt=datetime.datetime.now())

     return render(request, 'eventRegister.html', {
         'errors': [],
         'events': events,
         'isAllowToModify': isAllowToModify
     })


# Advising
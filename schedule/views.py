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

     if request.method == 'GET':
        # load the events data
          # events = Event.objects.filter(user=request.user)
          # create a test list of events
          events = [
               {
                    'title': 'Test Event 1',
                    'description': 'Huh',
                    'start_time': datetime.datetime(year_now, month_now, day_now, 10, 0, 0, 0, local_tzone),
                    'end_time': datetime.datetime(year_now, month_now, day_now, 11, 0, 0, 0, local_tzone)
               },
               {
                    'title': 'Test Event 2',
                    'description': 'This is a test event',
                    'start_time': datetime.datetime(year_now, month_now, day_now, 12, 0, 0, 0, local_tzone),
                    'end_time': datetime.datetime(year_now, month_now, day_now, 13, 0, 0, 0, local_tzone)
               },
               {
                    'title': 'Test Event 3',
                    'description': 'WTF',
                    'start_time': datetime.datetime(year_now, month_now, day_now, 14, 0, 0, 0, local_tzone),
                    'end_time': datetime.datetime(year_now, month_now, day_now, 15, 0, 0, 0, local_tzone)
               }
          ]

     return render(request, 'myEvents.html', {'events': events})

# Events

# Advising
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

     errors = Event.check()
     if(errors):
          return render(request, 'myEvents.html', 
                   {'errors': errors})
     
     if request.method == 'GET':
        # Get all events
            events = Event.objects.all()

     return render(request, 'myEvents.html', 
                   {'errors': []},
                   {'events': events}
                   )

# Events

# Advising
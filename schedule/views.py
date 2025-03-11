from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from users.models import Profile, Advisor

@login_required
def scheduleView(request):
    user = request.user
    
    try:
        profile = Profile.objects.get(user=user)
        advisor = Advisor.objects.get(user_id=profile)
        
        Events = listMyEvents(request)
        return render(request, 'scheduleView_advisor.html', {'profile': profile, 'events': Events})

    except Advisor.DoesNotExist:
        # user is not an advisor
        advisor = None
        Events = listMyEvents(request)
        return render(request, 'scheduleView.html', {'profile': profile, 'events': Events})

    except Profile.DoesNotExist:
        profile = None
        return render(request, 'scheduleView_DNE.html')
        
# myEvents
def listMyEvents(request):
    user = request.user
    
    try:
        profile = Profile.objects.get(user=user)
        events = Event.objects.filter(user_id=profile)
        consultation = Consultation.objects.filter(client_id=profile)
                                                    
        # combine events and consultation into one list
        myEvents = []
        for event in events:
            myEvents.append(event)
        for consult in consultation:
            myEvents.append(consult)
        return myEvents

    except Profile.DoesNotExist:
        return None
    

# Events

# Advising
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
        
        Events, Consultation = listMyEvents(request)
        return render(request, 'scheduleView_advisor.html', 
                      {'profile': profile,
                        'events': Events,
                        'consultations': Consultation})

    except Advisor.DoesNotExist:
        # user is not an advisor
        advisor = None
        Events, Consultation = listMyEvents(request)
        return render(request, 'scheduleView.html',
                      {'profile': profile,
                        'events': Events,
                        'consultations': Consultation})

    except Profile.DoesNotExist:
        profile = None
        return render(request, 'scheduleView_DNE.html')
        
# myEvents
def listMyEvents(request):
    user = request.user
    
    try:
        profile = Profile.objects.get(user=user)
        events = Event.objects.filter(user_id=profile)
        try:
            advisor = Advisor.objects.get(user_id=profile)
        except Advisor.DoesNotExist:
            advisor = None

        consultation = Consultation.objects.filter(advisor_id=advisor)
                                                    
        # combine events and consultation into one list
        myEvents = []
        myConsultation = []
        for event in events:
            myEvents.append(event)
        for consult in consultation:
            myConsultation.append(consult)
        return myEvents, myConsultation

    except Profile.DoesNotExist:
        return None
    

# Events

# Advising
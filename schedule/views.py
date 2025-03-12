from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
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


# Create new events
# Only advisors can create events
@login_required
def createNewEvent(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    
    if request.method == 'POST':
        start_timestamp = request.POST['start_timestamp']
        end_timestamp = request.POST['end_timestamp']
        
        # Convert string to datetime objects
        start_datetime = timezone.datetime.fromisoformat(start_timestamp)
        end_datetime = timezone.datetime.fromisoformat(end_timestamp)
        
        # Check if the dates are in the past
        # make_aware() is used to convert the datetime object to the timezone-aware datetime object
        if timezone.make_aware(start_datetime) < timezone.now() or timezone.make_aware(end_datetime) < timezone.now():
            error_message = "Start and End date must be in the future."
            return render(request, 'Advisor/createEvent.html', {
                'error_message': error_message,
                'title': request.POST['title'],
                'start_timestamp': start_timestamp,
                'end_timestamp': end_timestamp,
                'description': request.POST['description'],
                'location': request.POST['location'],
                'event_type': request.POST['event_type']
            })
        
        event = Event()
        event.user_id = profile
        event.registration_date = timezone.now()
        event.title = request.POST['title']
        event.event_start_timestamp = start_datetime
        event.event_end_timestamp = end_datetime
        event.description = request.POST['description']
        event.location = request.POST['location']
        event.event_type = request.POST['event_type']
        event.save()
        
        return redirect('view')
    else:
        return render(request, 'Advisor/createEvent.html')

@login_required
def modifyEvent(request, event_id):
    event = Event.objects.get(event_id=event_id)
    
    if request.method == 'POST':
        start_timestamp = request.POST['start_timestamp']
        end_timestamp = request.POST['end_timestamp']
        
        # Convert string to datetime objects
        start_datetime = timezone.datetime.fromisoformat(start_timestamp)
        end_datetime = timezone.datetime.fromisoformat(end_timestamp)
        
        # Check if the dates are in the past
        # make_aware() is used to convert the datetime object to the timezone-aware datetime object
        if timezone.make_aware(start_datetime) < timezone.now() or timezone.make_aware(end_datetime) < timezone.now():
            error_message = "Start and End date must be in the future."
            return render(request, 'Advisor/modifyEvent.html', {
                'error_message': error_message,
                'title': request.POST['title'],
                'start_timestamp': start_timestamp,
                'end_timestamp': end_timestamp,
                'description': request.POST['description'],
                'location': request.POST['location'],
                'event_type': request.POST['event_type'],
                'event': event  # Pass the event object to pre-fill the form
            })
        
        event.title = request.POST['title']
        event.event_start_timestamp = start_datetime
        event.event_end_timestamp = end_datetime
        event.description = request.POST['description']
        event.location = request.POST['location']
        event.event_type = request.POST['event_type']
        event.save()
        
        return redirect('view')
    else:
        return render(request, 'Advisor/modifyEvent.html', {
            'event': event,
            'title': event.title,
            'start_timestamp': event.event_start_timestamp.isoformat(),
            'end_timestamp': event.event_end_timestamp.isoformat(),
            'description': event.description,
            'location': event.location,
            'event_type': event.event_type
        })
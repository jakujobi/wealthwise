from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from .models import *
from users.models import Profile, Advisor
from .forms import *

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
        form = EventForm(request.POST)
        if form.is_valid():
            start_datetime = form.cleaned_data['event_start_timestamp']
            end_datetime = form.cleaned_data['event_end_timestamp']
            
            # Check if the dates are in the future
            if timezone.make_aware(start_datetime) < timezone.now() or timezone.make_aware(end_datetime) < timezone.now():
                error_message = "Start and End date must be in the future."
                return render(request, 'Advisor/createEvent.html', {
                    'form': form,
                    'error_message': error_message
                })
            
            event = form.save(commit=False)
            event.user_id = profile
            event.registration_date = timezone.now()
            event.save()
            
            return redirect('view')
    else:
        form = EventForm()
    
    return render(request, 'Advisor/createEvent.html', {'form': form})

@login_required
def modifyEvent(request, event_id):
    event = Event.objects.get(id=event_id)
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            start_datetime = form.cleaned_data['event_start_timestamp']
            end_datetime = form.cleaned_data['event_end_timestamp']
            
            # Check if the dates are in the future
            if timezone.make_aware(start_datetime) < timezone.now() or timezone.make_aware(end_datetime) < timezone.now():
                error_message = "Start and End date must be in the future."
                return render(request, 'Advisor/modifyEvent.html', {
                    'form': form,
                    'error_message': error_message,
                    'event': event
                })
            
            form.save()
            return redirect('view')
    else:
        form = EventForm(instance=event)
    
    return render(request, 'Advisor/modifyEvent.html', {'form': form, 'event': event})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from users.models import Profile, Advisor
from .forms import *

@login_required
def scheduleView(request,message=None):
    user = request.user
    
    try:
        profile = Profile.objects.get(user=user)
        advisor = Advisor.objects.get(user_id=profile)
        
        Events, Consultation = listMyEvents(request)
        return render(request, 'scheduleView_advisor.html', 
                      {'profile': profile,
                        'events': Events,
                        'consultations': Consultation,
                        'message': message})

    except Advisor.DoesNotExist:
        # user is not an advisor
        Events, Consultation = listMyEvents(request)
        return render(request, 'scheduleView.html',
                      {'profile': profile,
                        'events': Events,
                        'consultations': Consultation,
                        'message': message})

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
            if start_datetime < timezone.now() or end_datetime < timezone.now():
                error_message = "Start and End date must be in the future."
                return render(request, 'Advisor/createEvent.html', {
                    'form': form,
                    'title': form.cleaned_data['title'],
                    'description': form.cleaned_data['description'],
                    'location': form.cleaned_data['location'],
                    'event_start_timestamp': form.cleaned_data['event_start_timestamp'],
                    'event_end_timestamp': form.cleaned_data['event_end_timestamp'],
                    'error_message': error_message
                })
            
            if start_datetime > end_datetime:
                error_message = "End date must be after the start date."
                return render(request, 'Advisor/createEvent.html', {
                    'form': form,
                    'title': form.cleaned_data['title'],
                    'description': form.cleaned_data['description'],
                    'location': form.cleaned_data['location'],
                    'event_start_timestamp': form.cleaned_data['event_start_timestamp'],
                    'event_end_timestamp': form.cleaned_data['event_end_timestamp'],
                    'error_message': error_message
                })
            
            event = form.save(commit=False)
            event.user_id = profile
            event.registration_date = timezone.now()
            event.save()
            
            return redirect('view', message="Event Created successfully.")
        else:
            # Display form errors
            return render(request, 'Advisor/createEvent.html', {
                'form': form,
                'error_message': "There were errors in the form. Please correct them and try again.",
                'form_errors': form.errors
            })
    else:
        form = EventForm()
    
    return render(request, 'Advisor/createEvent.html', {'form': form})

@login_required
def eventDetail(request, eventId):
    try:
        event = Event.objects.get(event_id=eventId)
    except Event.DoesNotExist:
        event = None
    
    if request.method == "GET":
        return render(request, 'Advisor/eventDetails.html', {'event': event})
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            try:
                event = modifyEvent(event, form)
            except Exception as e:
                return render(request, 
                              'Advisor/eventDetails.html', 
                              {'event': event,
                               'error_message': str(e)})
            
            return redirect('view', message="Event updated successfully.")
        else:
            return render(request, 
                          'Advisor/eventDetails.html', 
                          {'event': event,
                           'error_message': "There were errors in the form. Please correct them and try again.",
                           'form_errors': form.errors})

def modifyEvent(event, form):
    
    start_datetime = form.cleaned_data['event_start_timestamp']
    end_datetime = form.cleaned_data['event_end_timestamp']
    
    # Check if the dates are in the future
    if start_datetime < timezone.now() or end_datetime < timezone.now():
        raise Exception("Start and End date must be in the future.")
    
    if start_datetime > end_datetime:
        raise Exception("End date must be after the start date.")

    event.title = form.cleaned_data['title']
    event.description = form.cleaned_data['description']
    event.location = form.cleaned_data['location']
    event.event_start_timestamp = start_datetime
    event.event_end_timestamp = end_datetime
    event.save()

    return event


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from users.models import Profile, Advisor
from .forms import *
from logging import getLogger
from django.utils.timezone import now

logger = getLogger(__name__)

userType = {
    'advisor': 'advisor',
    'admin': 'admin',
    'user': 'user'
}

# Authorize user
def authorizeUser(request):
    user = request.user
    try:
        # Check if user is an advisor
        try:
            profile = Profile.objects.get(user=user)
            advisor = Advisor.objects.get(user_id=profile)
            return userType['advisor']
        except Exception:
            # Is user an admin?
            if user.is_staff:
                return userType['admin']
            elif user.is_authenticated:
                # User is not an advisor or admin -> normal user
                return userType['user']
            
            raise Exception("User is unauthorized.")

    except Exception:
        logger.exception("Error during user authorization")
        return userType['user'] # Default to 'user' or raise an exception
    

@login_required
def scheduleView(request,message=None):
    user = request.user
    userTypeRequested = authorizeUser(request)
    
    try:
        if userTypeRequested == userType['advisor']:
            profile = Profile.objects.get(user=user)
            Events, Consultation = listMyEvents(user, userTypeRequested)
            return render(request, 'scheduleView_advisor.html', 
                        {'profile': profile,
                            'events': Events,
                            'consultations': Consultation,
                            'message': message})
        
        elif userTypeRequested == userType['admin']:
            profile = None
            Events, Consultation = listMyEvents(user, userTypeRequested)
            return render(request, 'scheduleView_advisor.html', 
                        {   'profile': profile,
                            'events': Events,
                            'consultations': Consultation,
                            'message': message})
        
        elif userTypeRequested == userType['user']:
            profile = Profile.objects.get(user=user)
            Events, Consultation = listMyEvents(user, userTypeRequested)

            return render(request, 'scheduleView.html', 
                        {'profile': profile,
                            'events': Events,
                            'consultations': Consultation,
                            'message': message})

    except Exception:
        logger.error("Error loading data for user: " + user.username + ". User Type: " + userTypeRequested)
        return redirect('errorPage', message="Something went wrong when loading your data. Please try again.")  

def errorPage(request, message=None):
    logger.error("Error: " + message + " Source user: " + request.user.username)
    return render(request, 'scheduleView_Error.html', {'message': message})

# myEvents
def listMyEvents(user, userTypeRequested):
    try:
        if userTypeRequested == userType['advisor']:
            profile = Profile.objects.get(user=user)
            advisor = Advisor.objects.get(user_id=profile)
            events = Event.objects.filter(user_id=profile, event_start_timestamp__gte=now())
            consultation = Consultation.objects.filter(advisor_id=advisor)

            # combine events and consultation into one list
            myEvents = []
            myConsultation = []
            for event in events:
                myEvents.append(event)
            for consult in consultation:
                myConsultation.append(consult)
            return myEvents, myConsultation
        
        elif userTypeRequested == userType['admin']:
            events = Event.objects.filter(event_start_timestamp__gte=now())
            consultation = Consultation.objects.filter()
            return events, consultation
        
        # TODO: Implement user view
        # elif userTypeRequested == userType['user']:
        #     profile = Profile.objects.get(user=user)

        #     events = Event.objects.filter(user_id=profile, event_start_timestamp__gte=now())
        #     consultation = Consultation.objects.filter(schedule_date_timestamp__gte=now())
        #     return events, consultation

        else:
            return None
                                                    
    except Profile.DoesNotExist:
        return None
    

# Events


# Create new events
# Only advisors can create events
@login_required
def createNewEvent(request):
    user = request.user
    userTypeRequested = authorizeUser(request)

    if userTypeRequested != userType['advisor'] and userTypeRequested != userType['admin']:
        return redirect('errorPage', message="You are not authorized to create events.")
    
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
    userTypeRequested = authorizeUser(request)

    if userTypeRequested != userType['advisor'] and userTypeRequested != userType['admin']:
        return redirect('errorPage', message="You are not authorized to view this page.")
    
    try:
        event = Event.objects.get(event_id=eventId)
    except Event.DoesNotExist:
        event = None
    
    if request.method == "GET":
        form = EventForm(initial={
            'title': event.title,
            'description': event.description,
            'location': event.location,
            'event_start_timestamp': event.event_start_timestamp,
            'event_end_timestamp': event.event_end_timestamp
        })
        return render(request, 'Advisor/eventDetails.html', {'event': event, 'form': form})
    
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

@login_required
def deleteEvent(request, eventId=None):
    userTypeRequested = authorizeUser(request)

    if userTypeRequested != userType['advisor'] and userTypeRequested != userType['admin']:
        return redirect('errorPage', message="You are not authorized to perform this action.")
    
    try:
        event = Event.objects.get(event_id=eventId)
        event.delete()
        return redirect('view', message="Event deleted successfully.")
    except Exception as e:
        return redirect('view.html', message= "Something wrong. Event does not exist. It may be already deleted.")
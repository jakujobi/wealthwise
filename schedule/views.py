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
        eventListRequest = request.POST.get('eventListRequest') if request.method == 'POST' else None
        if userTypeRequested == userType['advisor']:
            profile = Profile.objects.get(user=user)
            Events, Consultation = listMyEvents(user, userTypeRequested, eventListRequest=eventListRequest)
            return render(request, 'scheduleView_advisor.html', 
                          {'profile': profile,
                           'events': Events,
                           'consultations': Consultation,
                           'message': message,
                            'eventListRequest': eventListRequest
                        })                           
        
        elif userTypeRequested == userType['admin']:
            profile = None
            Events, Consultation = listMyEvents(user, userTypeRequested, eventListRequest=eventListRequest)
            return render(request, 'scheduleView_advisor.html', 
                          {'profile': profile,
                           'events': Events,
                           'consultations': Consultation,
                           'message': message,
                           'eventListRequest': eventListRequest})
        
        elif userTypeRequested == userType['user']:
            profile = Profile.objects.get(user=user)
            Events, Consultation = listMyEvents(user, userTypeRequested, eventListRequest=eventListRequest)
            return render(request, 'scheduleView_user.html', 
                          {'profile': profile,
                           'events': Events,
                           'consultations': Consultation,
                           'message': message,
                            'eventListRequest': eventListRequest
                           })
        
    except Exception as e:
        logger.error(f"Error loading data for user: {user.username}. User Type: {userTypeRequested}")
        logger.error(f"Error: {str(e)}")
        return redirect('errorPage', message="Something went wrong when loading your data.")  

def errorPage(request, message=None):
    logger.error("Error: " + message + " Source user: " + request.user.username)
    return render(request, 'scheduleView_Error.html', {'message': message})

# myEvents
def listMyEvents(user, userTypeRequested, eventListRequest=None):
    # event list request is used to filter the events list
    # if eventListRequest is None, return all events
    # if eventListRequest is not None, return events that match the request
    try:
        if userTypeRequested == userType['advisor']:
            
            profile = Profile.objects.get(user=user)
            advisor = Advisor.objects.get(user_id=profile)
            if eventListRequest == "PAST":
                events = Event.objects.filter(user_id=profile, event_start_timestamp__lt=now()).order_by('event_start_timestamp')
            elif eventListRequest == "UPCOMING":
                events = Event.objects.filter(user_id=profile, event_start_timestamp__gte=now()).order_by('event_start_timestamp')
            else:
                events = Event.objects.filter(user_id=profile).order_by('event_start_timestamp')
            consultation = Consultation.objects.filter(advisor_id=advisor)

            # combine events and consultation into one list
            myEvents = []
            myConsultation = []
            for event in events.order_by('event_start_timestamp'):
                myEvents.append(event)
            for consult in consultation:
                myConsultation.append(consult)
            return myEvents, myConsultation
        
        elif userTypeRequested == userType['admin']:
            
            if eventListRequest == "past":
                events = Event.objects.filter(event_start_timestamp__lt=now()).order_by('event_start_timestamp')
            elif eventListRequest == "upcoming":
                events = Event.objects.filter(event_start_timestamp__gte=now()).order_by('event_start_timestamp')
            else:
                events = Event.objects.all().order_by('event_start_timestamp')
            consultation = Consultation.objects.filter()
            return events, consultation
        
        elif userTypeRequested == userType['user']:
            profile = Profile.objects.get(user=user)

            # Fetch registered events for the user
            registered_events = eventRegistration.objects.filter(user_id=profile).select_related('event_id')

            if eventListRequest == "past":
                events = [reg.event_id for reg in registered_events if reg.event_id.event_start_timestamp < now()]
            elif eventListRequest == "upcoming":
                events = [reg.event_id for reg in registered_events if reg.event_id.event_start_timestamp >= now()]
            else:
                events = [reg.event_id for reg in registered_events]

            consultation = Consultation.objects.filter(client_id=profile, scheduled_date__gte=now())
            return events, consultation

        else:
            return None
                                                    
    except Exception as e:
        logger.error("Error loading events: " + str(e))
        return None

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
                error_message = "Start or End date must be in the future."
                return render(request, 'Advisor/createEvent.html', {
                    'form': form,
                    'title': form.cleaned_data['title'],
                    'description': form.cleaned_data['description'],
                    'location': form.cleaned_data['location'],
                    'event_start_timestamp': form.cleaned_data['event_start_timestamp'],
                    'event_end_timestamp': form.cleaned_data['event_end_timestamp'],
                    'error_message': error_message
                })
            
            if start_datetime >= end_datetime:
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
    
    if start_datetime >= end_datetime:
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



@login_required
def eventRegister_List(request):
    try:
        user = request.user
        profile = Profile.objects.get(user=user)
        events = Event.objects.order_by('event_start_timestamp').filter(scheduled_date__gte=now())
        registered_events = eventRegistration.objects.filter(user_id=profile).select_related('event_id')
    
        event_status = {}
        for event in events:
            event_status[event.event_id] = "None"

        for reg_event in registered_events:
            if reg_event.event_id.event_id in event_status:
                event_status[reg_event.event_id.event_id] = "Registered"

        for event in events:
            event.status = event_status.get(event.event_id, "None")

        return render(request, 'User/eventRegistration_list.html', {'events': events})
    except Exception as e:  
        logger.error(f"Error loading event registrations for user: {user.username}.")
        logger.error(f"Error: {str(e)}")
        return redirect('errorPage', message="Something went wrong when loading event data.")
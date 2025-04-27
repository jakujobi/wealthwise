from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from users.models import Profile, Advisor
from .forms import *
from logging import getLogger
from django.utils.timezone import now, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache
from django.db import transaction
from datetime import timedelta
import json

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
            advisor = Advisor.objects.get(user=user)
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
        eventListRequest = request.POST.get('eventListRequest') if request.method == 'POST' else "UPCOMING"
        if userTypeRequested == userType['advisor']:
            Events, Consultation = listMyEvents(user, userTypeRequested, eventListRequest=eventListRequest)
            availability = AdvisorAvailability.objects.filter(advisor=Advisor.objects.get(user=user)).first()
            time_slots = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
            if availability:
                for slot in availability.time_slots.all():
                    time_slots[slot.day_of_week].append(f"{slot.start_time} - {slot.end_time}")

            return render(request, 'scheduleView_advisor.html', {
                'user_first_name': user.first_name,
                'user_last_name': user.last_name,
                'events': Events,
                'consultations': Consultation,
                'message': message,
                'eventListRequest': eventListRequest,
                'time_slots': time_slots
            })
        
        elif userTypeRequested == userType['admin']:
            Events, Consultation = listMyEvents(user, userTypeRequested, eventListRequest=eventListRequest)
            return render(request, 'scheduleView_advisor.html', 
                          {
                           'user_first_name': user.first_name,
                           'user_last_name': user.last_name,
                           'events': Events,
                           'consultations': [{'client_name': f"{c.client_id.user.first_name} {c.client_id.user.last_name}",
                                              'scheduled_date': c.scheduled_date,
                                              'status': c.status,
                                              'consultation_id': c.consultation_id,
                                              'session_notes': c.session_notes} for c in Consultation],
                           'message': message,
                           'eventListRequest': eventListRequest})
        
        elif userTypeRequested == userType['user']:
            Events, Consultation = listMyEvents(user, userTypeRequested, eventListRequest=eventListRequest )
            return render(request, 'scheduleView_user.html', 
                          {
                           'user_first_name': user.first_name,
                           'user_last_name': user.last_name,
                           'events': Events,
                           'consultations': [{'advisor_name': f"{c.advisor_id.user.first_name} {c.advisor_id.user.last_name}", 
                                              'scheduled_date': c.scheduled_date, 
                                              'status': c.status,
                                              'consultation_id': c.consultation_id} for c in Consultation],
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
def listMyEvents(user, userTypeRequested, eventListRequest="UPCOMING"):
    # event list request is used to filter the events list
    # if eventListRequest is None, return all events
    # if eventListRequest is not None, return events that match the request
    try:
        if userTypeRequested == userType['advisor']:
            
            profile = Profile.objects.get(user=user)
            advisor = Advisor.objects.get(user=user)
            if eventListRequest.upper == "PAST":
                events = Event.objects.filter(user_id=profile, event_start_timestamp__lt=now()).order_by('event_start_timestamp')
            elif eventListRequest.upper == "UPCOMING":
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
            
            if eventListRequest.upper == "PAST":
                events = Event.objects.filter(event_start_timestamp__lt=now()).order_by('event_start_timestamp')
            elif eventListRequest.upper == "UPCOMING":
                events = Event.objects.filter(event_start_timestamp__gte=now()).order_by('event_start_timestamp')
            else:
                events = Event.objects.all().order_by('event_start_timestamp')
            consultation = Consultation.objects.filter()
            return events, consultation
        
        elif userTypeRequested == userType['user']:
            profile = Profile.objects.get(user=user)

            # Fetch registered events for the user
            registered_events = eventRegistration.objects.filter(user_id=profile).select_related('event_id')

            if eventListRequest.upper == "PAST":
                events = [reg.event_id for reg in registered_events if reg.event_id.event_start_timestamp < now()]
            elif eventListRequest.upper == "UPCOMING":
                events = [reg.event_id for reg in registered_events if reg.event_id.event_start_timestamp >= now()]
            else:
                events = [reg.event_id for reg in registered_events]

            # Exclude consultations that have passed the current day
            consultation = Consultation.objects.filter(
                client_id=profile,
                scheduled_date__gte=now()
            )
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
        events = Event.objects.order_by('event_start_timestamp').filter(event_start_timestamp__gte=now())
        registered_events = eventRegistration.objects.filter(user_id=profile).select_related('event_id')

        # Create a dictionary to store the status of each event
        event_status = {}
        for event in events:
            event_status[event.event_id] = ""

        # Check the status of each registered event and update the dictionary
        for reg_event in registered_events:
            if reg_event.event_id.event_id in event_status:
                event_status[reg_event.event_id.event_id] = "Registered"
            else:
                event_status[reg_event.event_id.event_id] = "Deleted"
        
        # Update the status of each event in the events list
        for event in events:
            event.status = event_status.get(event.event_id, "None")

        return render(request, 'User/eventRegister_list.html', {'events': events})
    except Exception as e:  
        logger.error(f"Error loading event registrations for user: {user.username}.")
        logger.error(f"Error: {str(e)}")
        return redirect('errorPage', message="Something went wrong when loading event data.")

@csrf_exempt
@require_POST
@never_cache
@login_required
def registerEvent(request, eventId=None):
    user = request.user
    userTypeRequested = authorizeUser(request)

    if userTypeRequested != userType['user']:
        return JsonResponse({'success': False, 'message': "You are not authorized to perform this action."}, status=403)
    
    try:
        profile = Profile.objects.get(user=user)
        event = Event.objects.get(event_id=eventId)

        # Check if the user is already registered for the event
        if eventRegistration.objects.filter(user_id=profile, event_id=event).exists():
            return JsonResponse({'success': False, 'message': "You are already registered for this event."}, status=400)

        # Register the user for the event
        registration = eventRegistration.objects.create(user_id=profile, event_id=event)
        return JsonResponse({'success': True, 'message': "Event registered successfully.", 'registration_id': registration.registration_id}, status=200)
    except Event.DoesNotExist:
        return JsonResponse({'success': False, 'message': "Event does not exist."}, status=404)
    except Exception as e:
        logger.error(f"Error registering for event: {eventId}. User: {user.username}.")
        logger.error(f"Error: {str(e)}")
        return JsonResponse({'success': False, 'message': "An error occurred while registering for the event."}, status=500)

@csrf_exempt
@require_POST
@never_cache
@login_required
def unregisterEvent(request, eventId=None):
    user = request.user
    userTypeRequested = authorizeUser(request)

    if userTypeRequested != userType['user']:
        return JsonResponse({'success': False, 'message': "You are not authorized to perform this action."}, status=403)
    
    try:
        profile = Profile.objects.get(user=user)
        event = Event.objects.get(event_id=eventId)

        with transaction.atomic():
            registration = eventRegistration.objects.filter(user_id=profile, event_id=event)
            if not registration.exists():
                return JsonResponse({'success': False, 'message': "You are not registered for this event."}, status=400)

            registration.delete()

        return JsonResponse({'success': True, 'message': "Event unregistered successfully."}, status=200)
    except Event.DoesNotExist:
        return JsonResponse({'success': False, 'message': "Event does not exist."}, status=404)
    except Exception as e:
        logger.error(f"Error unregistering from event: {eventId}. User: {user.username}. Exception: {str(e)}")
        return JsonResponse({'success': False, 'message': "An unexpected error occurred."}, status=500)

@login_required
def set_availability(request):
    userTypeRequested = authorizeUser(request)

    if userTypeRequested != userType['advisor']:
        return JsonResponse({'error_message': "You are not authorized to set availability."}, status=403)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_time_slots = data.get('time_slots', {})
            remove_time_slots = data.get('remove_time_slots', {})

            if not new_time_slots and not remove_time_slots:
                # Redirect to schedule view if no changes are made
                return JsonResponse({'redirect_url': '/schedule/view/'}, status=200)

            availability, created = AdvisorAvailability.objects.get_or_create(advisor=Advisor.objects.get(user=request.user))

            # Remove specified time slots
            for day, slots in remove_time_slots.items():
                for slot in slots:
                    availability.time_slots.filter(
                        day_of_week=day,
                        start_time=slot.get("start_time"),
                        end_time=slot.get("end_time")
                    ).delete()

            # Add new time slots
            for day, slots in new_time_slots.items():
                for slot in slots:
                    availability.time_slots.get_or_create(
                        day_of_week=day,
                        start_time=slot.get("start_time"),
                        end_time=slot.get("end_time")
                    )

            return JsonResponse({'redirect_url': '/schedule/view/Your%20available%20time%20slots%20saved'})
        except json.JSONDecodeError:
            return JsonResponse({'error_message': "Invalid time slots format."}, status=400)
    elif request.method == 'GET':
        # Retrieve previously saved time slots
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        availability = AdvisorAvailability.objects.filter(advisor=Advisor.objects.get(user=request.user)).first()
        time_slots = {day: [] for day in days_of_week}
        if availability:
            for slot in availability.time_slots.all():
                time_slots[slot.day_of_week].append({
                    "start_time": slot.start_time,
                    "end_time": slot.end_time
                })

        return render(request, 'Advisor/set_availability.html', {
            'availability': availability,
            'days_of_week': days_of_week,
            'time_slots': time_slots
        })
    else:
        return JsonResponse({'error_message': "Invalid request method."}, status=405)

@login_required
def get_availability(request, advisor_id):
    userTypeRequested = authorizeUser(request)

    if userTypeRequested != userType['user']:
        return JsonResponse({'error': 'You are not authorized to view availability.'}, status=403)

    try:
        availability = AdvisorAvailability.objects.filter(advisor_id=advisor_id)
        return JsonResponse({'availability': list(availability.values())}, status=200)
    except Exception as e:
        logger.error(f"Error retrieving availability: {str(e)}")
        return JsonResponse({'error': 'Could not retrieve availability.'}, status=500)

@login_required
def searchAdvisor(request):
    advisors_with_slots = []
    for advisor in Advisor.objects.all():
        # Fetch advisor rating directly from the Advisor model
        rating = advisor.rating
        advisors_with_slots.append({
            'advisor': advisor,
            'rating': round(rating, 1)  # Round to 1 decimal place
        })
    return render(request, 'User/searchAdvisor.html', {'advisors_with_slots': advisors_with_slots})

@login_required
def advisorAvailability(request, advisor_id):
    advisor = get_object_or_404(Advisor, id=advisor_id)
    week_offset = int(request.GET.get('week', 0))  # Get the week offset from the query parameter
    now = timezone.now()
    today = now.date()
    current_time = now.time()
    start_of_week = today + timedelta(weeks=week_offset, days=-today.weekday() - 1)  # Adjust to start from Sunday
    end_of_week = start_of_week + timedelta(days=6)

    # Prevent navigation to past weeks
    if start_of_week < today:
        week_offset = 0
        start_of_week = today + timedelta(days=-today.weekday() - 1)
        end_of_week = start_of_week + timedelta(days=6)

    availability = TimeSlot.objects.filter(
        availability__advisor=advisor,
        day_of_week__in=[(start_of_week + timedelta(days=i)).strftime('%A') for i in range(7)]
    )

    # Fetch booked time slots for the advisor within the week
    booked_slots = Consultation.objects.filter(
        advisor_id=advisor,
        scheduled_date__date__gte=start_of_week,
        scheduled_date__date__lte=end_of_week
    ).values_list('time_slot__day_of_week', 'time_slot__start_time', 'time_slot__end_time')

    weekly_availability = []
    for i in range(7):
        date = start_of_week + timedelta(days=i)
        day = date.strftime('%A')
        slots = [
            {
                "time_range": f"{slot.start_time.strftime('%I:%M %p')} - {slot.end_time.strftime('%I:%M %p')}",
                "is_booked": (day, slot.start_time, slot.end_time) in booked_slots,
                "is_past": (date < today) or (date == today and slot.start_time <= current_time and slot.end_time <= current_time),
                "date": date.strftime('%Y-%m-%d') 
            }
            for slot in availability.filter(day_of_week=day)
        ]
        weekly_availability.append((date, day, slots))

    context = {
        'advisor': advisor,
        'weekly_availability': weekly_availability,
        'time_slots': sorted(set(slot["time_range"] for _, _, slots in weekly_availability for slot in slots)),
        'today': today,  # Pass the current date to the template
        'previous_week': week_offset - 1 if week_offset > 0 else None,  # Disable previous week if at current week
        'current_week': 0,
        'next_week': week_offset + 1,
    }
    return render(request, 'User/advisorAvailability.html', context)

@login_required
def bookConsultation(request, advisor_id, time_slot):
    advisor = get_object_or_404(Advisor, id=advisor_id)
    selected_date = request.GET.get('date')
    try:
        # Decode and parse the time slot
        start_time, end_time = time_slot.split(" - ")
        start_time = timezone.datetime.strptime(start_time, "%I:%M %p").time()
        end_time = timezone.datetime.strptime(end_time, "%I:%M %p").time()
        scheduled_date = timezone.datetime.strptime(selected_date, "%Y-%m-%d").date()
    except ValueError:
        return redirect('errorPage', message="Invalid time slot or date format.")

    if request.method == 'POST':
        # Save the consultation to the database
        time_slot_obj = TimeSlot.objects.filter(
            availability__advisor=advisor,
            start_time=start_time,
            end_time=end_time
        ).first()

        if not time_slot_obj:
            return redirect('errorPage', message="Time slot not available.")

        Consultation.objects.create(
            client_id=request.user.profile,
            advisor_id=advisor,
            scheduled_date=timezone.datetime.combine(scheduled_date, start_time),
            time_slot=time_slot_obj,
            status="Scheduled"
        )
        return redirect('view', message="Consultation booked successfully.")

    return render(request, 'User/bookConsultation.html', {
        'advisor': advisor,
        'time_slot': f"{start_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}",
        'scheduled_date': selected_date
    })

@login_required
def cancelConsultation(request, consultation_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_notes = data.get('session_notes', '')

            consultation = Consultation.objects.get(consultation_id=consultation_id)

            # Determine the cancellation reason based on the user type
            userTypeRequested = authorizeUser(request)
            if userTypeRequested == userType['user']:
                cancellation_reason = "Cancelled By User"
            elif userTypeRequested == userType['advisor']:
                cancellation_reason = "Cancelled By Advisor"
            else:
                return JsonResponse({'success': False, 'message': "You are not authorized to cancel this consultation."}, status=403)

            # Check if the user is authorized to cancel
            if userTypeRequested == userType['user'] and request.user.profile != consultation.client_id:
                return JsonResponse({'success': False, 'message': "You are not authorized to cancel this consultation."}, status=403)

            consultation.status = cancellation_reason
            consultation.session_notes += session_notes  # Save session notes if provided
            consultation.save()

            return JsonResponse({'success': True, 'message': "Consultation cancelled successfully."}, status=200)
        except Consultation.DoesNotExist:
            return JsonResponse({'success': False, 'message': "Consultation does not exist."}, status=404)
        except Exception as e:
            logger.error(f"Error cancelling consultation: {consultation_id}. User: {request.user.username}. Exception: {str(e)}")
            return JsonResponse({'success': False, 'message': "An unexpected error occurred."}, status=500)
    else:
        return JsonResponse({'success': False, 'message': "Invalid request method."}, status=405)
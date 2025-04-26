from django.contrib import admin
from .models import Consultation, Event, AdvisorAvailability, TimeSlot, eventRegistration

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('consultation_id', 'client_id', 'advisor_id', 'scheduled_date', 'status')
    search_fields = ('consultation_id', 'client_id__user__username', 'advisor_id__user__username', 'status')

admin.site.register(Consultation, ConsultationAdmin)

class TimeSlotInline(admin.TabularInline):
    model = TimeSlot
    extra = 1  # Number of empty slots to display for adding new ones

class AdvisorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('advisor', 'get_blocked_slots_count')
    search_fields = ('advisor__user__username',)
    inlines = [TimeSlotInline]

    def get_blocked_slots_count(self, obj):
        return len(obj.blockedDateTime or [])
    get_blocked_slots_count.short_description = "Blocked Slots Count"

admin.site.register(AdvisorAvailability, AdvisorAvailabilityAdmin)

class EventAdmin(admin.ModelAdmin):
    # list of fields to display in the admin panel
    list_display = ('event_id', 'title', 'event_start_timestamp', 'event_end_timestamp', 'location')
    
    # list of fields to filter by in the admin panel
    list_filter = ('event_start_timestamp', 'event_end_timestamp', 'location')
    
    # list of fields to search by in the admin panel
    search_fields = ( 'event_id', 'title', 'location')

admin.site.register(Event, EventAdmin)

class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('get_event_title', 'get_registered_users', 'status', 'registration_date_time')
    list_filter = ('event_id',)  # Filter by event
    search_fields = ('event_id__title', 'user_id__user__username', 'status')

    def get_event_title(self, obj):
        return obj.event_id.title
    get_event_title.short_description = "Event Title"

    def get_registered_users(self, obj):
        return ", ".join([registration.user_id.user.username for registration in eventRegistration.objects.filter(event_id=obj.event_id)])
    get_registered_users.short_description = "Registered Users"

admin.site.register(eventRegistration, EventRegistrationAdmin)
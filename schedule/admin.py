from django.contrib import admin
from .models import Consultation, Event

# Register your models here.
admin.site.register(Consultation)

class EventAdmin(admin.ModelAdmin):
    # list of fields to display in the admin panel
    list_display = ('event_id', 'title', 'event_start_timestamp', 'event_end_timestamp', 'location')
    
    # list of fields to filter by in the admin panel
    list_filter = ('event_start_timestamp', 'event_end_timestamp', 'location')
    
    # list of fields to search by in the admin panel
    search_fields = ('title', 'location')

admin.site.register(Event, EventAdmin)

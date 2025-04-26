from django.urls import path
from .views import *

urlpatterns = [
    path('view/', scheduleView, name='view'),
    path('view/<str:message>', scheduleView, name='view'),
    path('createEvent/', createNewEvent, name='createEvent'),
    path('eventDetail/<str:eventId>/', eventDetail, name='eventDetail'),
    path('deleteEvent/<str:eventId>/', deleteEvent, name='deleteEvent'),
    path('error/<str:message>', errorPage, name='errorPage'),
    path('eventRegister', eventRegister_List, name='eventRegister'),
    path('registerEvent/<int:eventId>/', registerEvent, name='registerEvent'),
    path('unregister/<int:eventId>/', unregisterEvent, name='unregisterEvent'),
    path('setAvailability/', set_availability, name='setAvailability'),
    path('searchAdvisor/', searchAdvisor, name='searchAdvisor'),
    path('advisorAvailability/<int:advisor_id>/', advisorAvailability, name='advisorAvailability'),
    path('bookConsultation/<int:advisor_id>/<str:time_slot>/', bookConsultation, name='bookConsultation'),
]
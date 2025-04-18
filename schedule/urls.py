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
]
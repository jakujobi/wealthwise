from django.urls import path
from .views import *

urlpatterns = [
    path('view/', scheduleView, name='view'),
    path('createEvent/', createNewEvent, name='createEvent'),
]
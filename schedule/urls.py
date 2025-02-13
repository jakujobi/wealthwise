from django.urls import path
from .views import myEvents

urlpatterns = [

     path('myEvents/', myEvents, name='myEvents')

]
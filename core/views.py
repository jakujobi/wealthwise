# core/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def custom_404_view(request, exception):
    return render(request, 'HTTP_404.html', status=404)

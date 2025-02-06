# core/views.py
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to WealthWise!</h1><p>Go to /calculators/loan/ to see the loan calculator.</p>")

# calculators/urls.py
from django.urls import path
from .views import loan_calculator

urlpatterns = [
    path('loan/', loan_calculator, name='loan_calculator'),
]
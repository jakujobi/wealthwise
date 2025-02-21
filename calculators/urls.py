# calculators/urls.py
from django.urls import path
from .views import (
    calculators_home,
    loan_calculator,
    mortgage_calculator,
    budgeting_tool,
    retirement_calculator,
    insurance_calculator,
    student_loan_calculator,
    car_payment_calcualtor
)

urlpatterns = [
    path('', calculators_home, name='calculators_home'),
    path('loan/', loan_calculator, name='loan_calculator'),
    path('mortgage/', mortgage_calculator, name='mortgage_calculator'),
    path('budgeting/', budgeting_tool, name='budgeting_tool'),
    path('retirement/', retirement_calculator, name='retirement_calculator'),
    path('insurance/', insurance_calculator, name='insurance_calculator'),
    path('student-loan/', student_loan_calculator, name='student_loan_calculator'),
    path('car-payment/', car_payment_calcualtor, name='car_payment_calcualtor'),
]
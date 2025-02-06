# calculators/views.py
from django.shortcuts import render
import math

def loan_calculator(request):
    monthly_payment = None
    total_interest = None

    if request.method == 'POST':
        # 1. Get form data
        loan_amount = float(request.POST.get('loan_amount'))
        interest_rate = float(request.POST.get('interest_rate')) / 100.0 / 12.0
        loan_term = int(request.POST.get('loan_term')) * 12  # Convert years to months

        # 2. Calculate monthly payment (amortization formula)
        if interest_rate == 0:
            # no interest case
            monthly_payment = loan_amount / loan_term
        else:
            numerator = interest_rate * ((1 + interest_rate) ** loan_term)
            denominator = ((1 + interest_rate) ** loan_term) - 1
            monthly_payment = loan_amount * (numerator / denominator)

        # 3. Calculate total interest
        total_paid = monthly_payment * loan_term
        total_interest = total_paid - loan_amount

        # Round results
        monthly_payment = round(monthly_payment, 2)
        total_interest = round(total_interest, 2)

    return render(request, 'calculators/loan_calculator.html', {
        'monthly_payment': monthly_payment,
        'total_interest': total_interest,
    })

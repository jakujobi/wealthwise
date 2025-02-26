# calculators/views.py
from django.shortcuts import render
import math

# Add new calculators homepage view
def calculators_home(request):
    return render(request, 'calculators.html')

def loan_calculator(request):
    monthly_payment = None
    total_interest = None

    if request.method == 'POST':
        # 1. Get form data
        loan_amount = float(request.POST.get('loan_amount'))
        interest_rate = (1 + (float(request.POST.get('interest_rate')) / 100)) ** (1/12) - 1
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

    return render(request, 'loan_calculator.html', {
        'monthly_payment': monthly_payment,
        'total_interest': total_interest
    })

def mortgage_calculator(request):
    monthly_payment = None
    principle_amount = None
    interest_amount = None
    down_payment_adj = None
    down_payment_adj_PA = None
    down_payment_adj_IA = None
    interest_rate_adj_disp = None
    interest_rate_adj_PA = None
    interest_rate_adj_IA = None

    if request.method == "POST":
        home_price = float(request.POST.get('home_price'))
        down_payment = float(request.POST.get('down_payment'))
        interest_rate = (1 + (float(request.POST.get('interest_rate')) / 100)) ** (1/12) - 1
        loan_term = float(request.POST.get('loan_term')) * 12

        # Baseline calculation
        principle_amount = home_price - down_payment

        if interest_rate == 0:
            monthly_payment = principle_amount / loan_term
        else:
            numerator = interest_rate * ((1 + interest_rate) ** loan_term)
            denominator = ((1 + interest_rate) ** loan_term) - 1
            monthly_payment = principle_amount * (numerator / denominator)
        
        total_payment = monthly_payment * loan_term
        interest_amount = total_payment - principle_amount

        # New down payment
        down_payment_adj = min(down_payment * 1.3, home_price)

        down_payment_adj_PA = home_price - down_payment_adj

        if interest_rate == 0:
            monthly_payment_DP = down_payment_adj_PA / loan_term
        else:
            numerator = interest_rate * ((1 + interest_rate) ** loan_term)
            denominator = ((1 + interest_rate) ** loan_term) - 1
            monthly_payment_DP = down_payment_adj_PA * (numerator / denominator)
        
        total_payment = monthly_payment_DP * loan_term
        down_payment_adj_IA = total_payment - down_payment_adj_PA

        # New interest rate
        interest_rate_adj = max(interest_rate * .8, 0)
        interest_rate_adj_disp = interest_rate_adj * 100 * 12

        interest_rate_adj_PA = home_price - down_payment

        if interest_rate_adj == 0:
            monthly_payment_IR = interest_rate_adj_PA / loan_term
        else:
            numerator = interest_rate_adj * ((1 + interest_rate_adj) ** loan_term)
            denominator = ((1 + interest_rate_adj) ** loan_term) - 1
            monthly_payment_IR = interest_rate_adj_PA * (numerator / denominator)
        
        total_payment = monthly_payment_IR * loan_term
        interest_rate_adj_IA = total_payment - interest_rate_adj_PA

    return render(request, 'mortgage_calculator.html', {
        'monthly_payment': monthly_payment,
        'principle_amount': principle_amount,
        'interest_amount': interest_amount,
        'down_payment_adj': down_payment_adj,
        'down_payment_adj_PA': down_payment_adj_PA,
        'down_payment_adj_IA': down_payment_adj_IA,
        'interest_rate_adj': interest_rate_adj_disp,
        'interest_rate_adj_PA': interest_rate_adj_PA,
        'interest_rate_adj_IA': interest_rate_adj_IA
    })
    
def budgeting_tool(request):
    overspend_areas = ""
    savings_goal_message = ''

    if request.method == 'POST':
        fixed_income = float(request.POST.get('fixed_income'))
        variable_income = float(request.POST.get('variable_income'))

        one_year_savings_goal = float(request.POST.get('one_year_savings_goal'))

        expenses = {
            'housing': float(request.POST.get('housing')),
            'taxes': float(request.POST.get('taxes')),
            'car_payment': float(request.POST.get('car_payment')),
            'internet_phone': float(request.POST.get('internet_phone')),
            'subscriptions': float(request.POST.get('subscriptions')),
            'food': float(request.POST.get('food')),
            'entertainment': float(request.POST.get('entertainment')),
            'personal_items': float(request.POST.get('personal_items')),
            'utilities': float(request.POST.get('utilities')),
            'transportation': float(request.POST.get('transportation')),
            'medical': float(request.POST.get('medical')),
            'misc': float(request.POST.get('misc'))
        }
        spending_thresholds = {
            'housing': .30,
            'taxes': .30,
            'car_payment': .125,
            'internet_phone': .03,
            'subscriptions': .02,
            'food': .125,
            'entertainment': .075,
            'personal_items': .035,
            'utilities': .075,
            'transportation': .075,
            'medical': .075,
            'misc': .03
        }

        total_income = fixed_income + variable_income
        total_expenses = sum(expenses.values())

        for category, amount in expenses.items():
            if amount > spending_thresholds.get(category) * total_income:
                overspend_areas += ("Spending in {} exceeds recomended value of {}%.\n").format(category, spending_thresholds.get(category) * 100)

        if (total_income - total_expenses) * 12 < one_year_savings_goal:
            savings_goal_message = "Your current spending exceeds your savings goal. You will have ${} by the end of a year. Consider reducing expenses, especially in any highlighted areas.".format((total_income - total_expenses) * 12)
        else:
            savings_goal_message = "You are on track to meet your savings goal! You will have ${} by the end of a year!".format((total_income - total_expenses) * 12)

    return render(request, 'budgeting_tool.html', {
        'overspend_areas': overspend_areas,
        'savings_goal_message': savings_goal_message
    })

def retirement_calculator(request):
    expected_savings = None
    meet_goal = None
    payment_to_meet_goal = None

    if request.method == 'POST':
        current_age = float(request.POST.get('current_age'))
        retirement_age = float(request.POST.get('retirement_age'))
        present_savings = float(request.POST.get('present_savings'))
        monthly_contributions = float(request.POST.get('monthly_contributions'))
        rate_of_return = (1 + (float(request.POST.get('rate_of_return')) / 100)) ** (1/12) - 1
        retirement_goal = float(request.POST.get('retirement_goal'))

        months_to_retirement = (retirement_age - current_age) * 12

        expected_savings = present_savings * ((1 + rate_of_return) ** months_to_retirement)

        expected_savings += monthly_contributions * (((1 + rate_of_return) ** months_to_retirement - 1) / rate_of_return) * (1 + rate_of_return)

        meet_goal = expected_savings >= retirement_goal

        if not meet_goal:
            required_savings = retirement_goal - present_savings * ((1 + rate_of_return) ** months_to_retirement)
            payment_to_meet_goal = required_savings * (rate_of_return / ((1 + rate_of_return) ** months_to_retirement - 1))
        else:
            payment_to_meet_goal = 0

    return render(request, 'retirement_calculator.html', {
        'expected_savings': expected_savings,
        'meet_goal': meet_goal,
        'payment_to_meet_goal': payment_to_meet_goal
    })

def insurance_calculator(request):
    option1_avg_cost = None
    option2_avg_cost = None
    option3_avg_cost = None
    best_option = None

    if request.method == 'POST':
        option1_cost = float(request.POST.get('option1_cost'))
        option2_cost = float(request.POST.get('option2_cost'))
        option3_cost = float(request.POST.get('option3_cost'))
        option1_coverage = float(request.POST.get('option1_coverage'))
        option2_coverage = float(request.POST.get('option2_coverage'))
        option3_coverage = float(request.POST.get('option3_coverage'))
        accident_probability = float(request.POST.get('accident_probability'))
        accident_cost = float(request.POST.get('accident_cost'))

        option1_avg_cost = option1_cost + accident_probability * (accident_cost - option1_coverage)
        option2_avg_cost = option2_cost + accident_probability * (accident_cost - option2_coverage)
        option3_avg_cost = option3_cost + accident_probability * (accident_cost - option3_coverage)
        
        if option1_avg_cost <= option2_avg_cost and option1_avg_cost <= option3_avg_cost:
            best_option = 'Option 1'
        elif option2_avg_cost <= option1_avg_cost and option2_avg_cost <= option3_avg_cost:
            best_option = 'Option 2'
        elif option3_avg_cost <= option1_avg_cost and option3_avg_cost <= option2_avg_cost:
            best_option = 'Option 3'

    return render(request, 'insurance_calculator.html', {
        'option1_avg_cost': option1_avg_cost,
        'option2_avg_cost': option2_avg_cost,
        'option3_avg_cost': option3_avg_cost,
        'best_option': best_option
    })

def student_loan_calculator(request):
    monthly_payment = None
    total_interest = None
    total_cost = None
    adjusted_term = None
    monthly_payment_adj_term = None
    total_interest_adj_term = None
    total_cost_adj_term = None

    if request.method == 'POST':
        loan_amount = float(request.POST.get('loan_amount'))
        interest_rate = (1 + (float(request.POST.get('interest_rate')) / 100)) ** (1/12) - 1
        loan_term = int(request.POST.get('loan_term')) * 12  # Convert years to months

        if interest_rate == 0:
            monthly_payment = loan_amount / loan_term
        else:
            numerator = interest_rate * ((1 + interest_rate) ** loan_term)
            denominator = ((1 + interest_rate) ** loan_term) - 1
            monthly_payment = loan_amount * (numerator / denominator)

        total_cost = monthly_payment * loan_term
        total_interest = total_cost - loan_amount

        adjusted_term_years = loan_term / 2
        adjusted_term = adjusted_term_years * 12

        monthly_payment_adj_term = loan_amount * interest_rate / (1 - (1 + interest_rate) ** - adjusted_term)
        total_cost_adj_term = monthly_payment_adj_term * adjusted_term
        total_interest_adj_term = total_cost_adj_term - loan_amount

    return render(request, 'student_loan_calculator.html', {
        'monthly_payment': monthly_payment,
        'total_interest': total_interest,
        'total_cost': total_cost,
        'adjusted_term': adjusted_term,
        'monthly_payment_adj_term': monthly_payment_adj_term,
        'total_interest_adj_term': total_interest_adj_term,
        'total_cost_adj_term': total_cost_adj_term
    })

def car_payment_calculator(request):
    monthly_payment = None
    total_interest = None
    total_cost = None
    adjust_double_initial_payment = None
    monthly_payment_adj_pay = None
    total_interest_adj_pay = None
    total_cost_adj_pay = None

    if request.method == 'POST':
        loan_amount = float(request.POST.get('loan_amount'))
        interest_rate = (1 + (float(request.POST.get('interest_rate')) / 100)) ** (1/12) - 1
        down_payment = float(request.POST.get('down_payment'))
        loan_term = int(request.POST.get('loan_term')) * 12  # Convert years to months

        # Base calcualtion
        loan_principal = loan_amount - down_payment
        if interest_rate == 0:
            monthly_payment = loan_principal / loan_term
        else:
            numerator = interest_rate * ((1 + interest_rate) ** loan_term)
            denominator = ((1 + interest_rate) ** loan_term) - 1
            monthly_payment = loan_principal * (numerator / denominator)
        total_cost = monthly_payment * loan_term
        total_interest = total_cost - loan_principal

        # Doubled down Payment
        adjust_double_initial_payment = down_payment * 2
        loan_principal_adj = loan_amount - adjust_double_initial_payment
        if interest_rate == 0:
            monthly_payment_adj_pay = loan_principal_adj / loan_term
        else:
            numerator = interest_rate * ((1 + interest_rate) ** loan_term)
            denominator = ((1 + interest_rate) ** loan_term) - 1
            monthly_payment_adj_pay = loan_principal_adj * (numerator / denominator)
        total_cost_adj_pay = monthly_payment_adj_pay * loan_term
        total_interest_adj_pay = total_cost_adj_pay - loan_principal_adj

    return render(request, 'car_payment_calculator.html', {
        'monthly_payment': monthly_payment,
        'total_interest': total_interest,
        'total_cost': total_cost,
        'adjust_double_initial_payment': adjust_double_initial_payment,
        'monthly_payment_adj_pay': monthly_payment_adj_pay,
        'total_interest_adj_pay': total_interest_adj_pay,
        'total_cost_adj_pay': total_cost_adj_pay
    })

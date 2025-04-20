# calculators/views.py
from django.contrib import messages
from django.shortcuts import render
from .models import FinancialToolUsage
from users.models import Subscription
from datetime import date, datetime
import json
from django.utils.timezone import now

# Add new calculators homepage view
def calculators_home(request):
    return render(request, 'calculators.html')

def loan_calculator(request):
    monthly_payment = None
    total_interest = None
    loan_amount = None
    interest_rate = None
    loan_term = None
    total_cost = None
    total_payments = None
    principal_percentage = None
    interest_percentage = None

    if request.method == 'POST':
        # 1. Get form data
        loan_amount = float(request.POST.get('loan_amount'))
        interest_rate_annual = float(request.POST.get('interest_rate'))
        interest_rate = (1 + (interest_rate_annual / 100)) ** (1/12) - 1
        loan_term_years = int(request.POST.get('loan_term'))
        loan_term = loan_term_years * 12  # Convert years to months

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
        
        # 4. Calculate additional metrics for enhanced display
        total_cost = loan_amount + total_interest
        total_payments = loan_term
        
        # 5. Calculate percentages for the payment breakdown chart
        principal_percentage = round((loan_amount / total_cost) * 100)
        interest_percentage = round((total_interest / total_cost) * 100)

        # Round results
        monthly_payment = round(monthly_payment, 2)
        total_interest = round(total_interest, 2)
        total_cost = round(total_cost, 2)

    return render(request, 'loan_calculator.html', {
        'monthly_payment': monthly_payment,
        'total_interest': total_interest,
        'loan_amount': loan_amount,
        'interest_rate': interest_rate_annual if 'interest_rate_annual' in locals() else None,
        'loan_term': loan_term_years if 'loan_term_years' in locals() else None,
        'total_cost': total_cost,
        'total_payments': total_payments,
        'principal_percentage': principal_percentage,
        'interest_percentage': interest_percentage
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

        # Round results
        monthly_payment = round(monthly_payment, 2)
        principle_amount = round(principle_amount, 2)
        interest_amount = round(interest_amount, 2)
        down_payment_adj = round(down_payment_adj, 2)
        down_payment_adj_PA = round(down_payment_adj_PA, 2)
        down_payment_adj_IA = round(down_payment_adj_IA, 2)
        interest_rate_adj_disp = round(interest_rate_adj_disp, 2)
        interest_rate_adj_PA = round(interest_rate_adj_PA, 2)
        interest_rate_adj_IA = round(interest_rate_adj_IA, 2)

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
    overspend_areas = ''
    savings_goal_message = ''
    previous_entries = None
    form_data = {}

    # Ensuser User is logged in
    if request.user.is_anonymous or not hasattr(request.user, 'profile'):
        messages.error(request, "Warning: You must be logged in to use this calculator.")
        return render(request, 'budgeting_tool.html', {
                'overspend_areas': overspend_areas,
                'savings_goal_message': savings_goal_message,
                'previous_entries': previous_entries,
                'form_data': form_data
            })
    
    # Get user profile for various later operations
    profile = request.user.profile
    
    # Ensuser User is subscribed
    if not Subscription.objects.filter(user_id=profile, start_date__lte=now(), end_date__gte=now()).exists():
        messages.error(request, "Warning: You must have an active subscription to use this calculator.")
        return render(request, 'budgeting_tool.html', {
                'overspend_areas': overspend_areas,
                'savings_goal_message': savings_goal_message,
                'previous_entries': previous_entries,
                'form_data': form_data
            })

    # Retrieve entries to load into Previous Results after unpacking
    raw_entries = FinancialToolUsage.objects.filter(user_id = profile).order_by('-budget_for_date')
    previous_entries = loadEntriesFromDB(request, raw_entries)

    # Method specific code
    if request.method == 'POST':
        if request.POST['action'] == 'load':
            entry_id = request.POST.get('entry_id')
            entry = raw_entries.get(usage_id=entry_id)

            # Set up json input as dictionary and input non-comple fields (not expenses in list or date fields)
            form_data = json.loads(entry.input_data)

            # Extract and flatten expenses into form_data
            expenses = form_data.get('expenses')
            for key in ['housing', 'taxes', 'car_payment', 'internet_phone', 'subscriptions', 
                        'food', 'entertainment', 'personal_items', 'utilities', 
                        'transportation', 'medical', 'misc']:
                form_data[key] = expenses.get(key)

            # Add budget month and year
            form_data['budget_month'] = entry.budget_for_date.month
            form_data['budget_year'] = entry.budget_for_date.year

            return render(request, 'budgeting_tool.html', {
                'overspend_areas': overspend_areas,
                'savings_goal_message': savings_goal_message,
                'previous_entries': previous_entries,
                'form_data': form_data
            })
        elif request.POST['action'] == 'delete':
            entry_id = request.POST.get('entry_id')
            profile = request.user.profile

            try:
                # Retrieve the entry by ID and ensure it belongs to the current user
                entry = FinancialToolUsage.objects.get(user_id=profile, usage_id=entry_id)
                entry.delete()  # Delete the entry from the database
            except FinancialToolUsage.DoesNotExist:
                # Handle the case where the entry does not exist (e.g., invalid ID)
                pass

            profile = request.user.profile
            raw_entries = FinancialToolUsage.objects.filter(user_id=profile).order_by('-budget_for_date')

            previous_entries = loadEntriesFromDB(request, raw_entries)

            return render(request, 'budgeting_tool.html', {
                'overspend_areas': overspend_areas,
                'savings_goal_message': savings_goal_message,
                'previous_entries': previous_entries,
                'form_data': form_data
            })
        
        # Save data in fields for use and re-population upon return from request
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

        budget_month = int(request.POST.get('budget_month'))
        budget_year = int(request.POST.get('budget_year'))

        input_data = {
            'fixed_income': fixed_income,
            'variable_income': variable_income,
            'one_year_savings_goal': one_year_savings_goal,
            'expenses': expenses
        }
        form_data['fixed_income'] = fixed_income
        form_data['variable_income'] = variable_income
        form_data['one_year_savings_goal'] = one_year_savings_goal

        for key in ['housing', 'taxes', 'car_payment', 'internet_phone', 'subscriptions', 
                    'food', 'entertainment', 'personal_items', 'utilities', 
                    'transportation', 'medical', 'misc']:
            form_data[key] = expenses.get(key)

        form_data['budget_month'] = budget_month
        form_data['budget_year'] = budget_year

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
                overspend_areas += ("Spending in {} exceeds recommended value of {}%.\n").format(category, round(spending_thresholds.get(category) * 100, 2))

        if (total_income - total_expenses) * 12 < one_year_savings_goal:
            savings_goal_message = "Your current spending exceeds your savings goal. You will have ${} in a year. Consider reducing expenses, especially in any highlighted areas.".format(round((total_income - total_expenses) * 12, 2))
        else:
            savings_goal_message = "You are on track to meet your savings goal! You will have ${} in a year!".format(round((total_income - total_expenses) * 12, 2))

        if request.POST['action'] == 'save':
            profile = request.user.profile
            budget_date = date(budget_year, budget_month, 1)

            # Check if an entry with the same budget_for_date exists
            existing_entry = FinancialToolUsage.objects.filter(
                user_id=profile,
                tool_type='budget_tool',
                budget_for_date=budget_date
            ).first()

            if existing_entry:
                # If an entry exists, update it
                existing_entry.input_data = json.dumps(input_data)
                existing_entry.usage_date = datetime.now()  # Update the timestamp
                existing_entry.save()
            else:
                # If no entry exists, create a new one
                financial_tool_usage = FinancialToolUsage(
                    user_id=profile,
                    tool_type='budget_tool',
                    input_data=json.dumps(input_data),
                    usage_date=datetime.now(),
                    budget_for_date=budget_date
                )
                financial_tool_usage.save()

            profile = request.user.profile
            raw_entries = FinancialToolUsage.objects.filter(user_id=profile).order_by('-budget_for_date')

            previous_entries = loadEntriesFromDB(request, raw_entries)

    return render(request, 'budgeting_tool.html', {
        'overspend_areas': overspend_areas,
        'savings_goal_message': savings_goal_message,
        'previous_entries': previous_entries,
        'form_data': form_data
    })

def retirement_calculator(request):
    expected_savings = None
    meet_goal = ''
    payment_to_meet_goal = None
    additional_savings_needed = None
    monthly_contributions = 0

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

        meet_goal_bool = expected_savings >= retirement_goal

        if not meet_goal_bool:
            required_savings = retirement_goal - present_savings * ((1 + rate_of_return) ** months_to_retirement)
            payment_to_meet_goal = required_savings * (rate_of_return / ((1 + rate_of_return) ** months_to_retirement - 1))
            additional_savings_needed = payment_to_meet_goal - monthly_contributions
        else:
            payment_to_meet_goal = 0
            additional_savings_needed = 0
        
        # Round Results
        expected_savings = round(expected_savings, 2)
        if meet_goal_bool:
            meet_goal = 'Yes'
        else:
            meet_goal = 'No'
        payment_to_meet_goal = round(payment_to_meet_goal, 2)
        additional_savings_needed = round(additional_savings_needed, 2)

    return render(request, 'retirement_calculator.html', {
        'expected_savings': expected_savings,
        'meet_goal': meet_goal,
        'payment_to_meet_goal': payment_to_meet_goal,
        'monthly_contributions': monthly_contributions,
        'additional_savings_needed': additional_savings_needed,
        'retirement_goal': retirement_goal if request.method == 'POST' else None
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

        # Round Results
        option1_avg_cost = round(option1_avg_cost, 2)
        option2_avg_cost = round(option2_avg_cost, 2)
        option3_avg_cost = round(option3_avg_cost, 2)

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

        adjusted_term = loan_term / 2

        monthly_payment_adj_term = loan_amount * interest_rate / (1 - (1 + interest_rate) ** -adjusted_term)
        total_cost_adj_term = monthly_payment_adj_term * adjusted_term
        total_interest_adj_term = total_cost_adj_term - loan_amount

        # Round results
        monthly_payment = round(monthly_payment, 2)
        total_interest = round(total_interest, 2)
        total_cost = round(total_cost, 2)
        adjusted_term = round(adjusted_term, 2)
        monthly_payment_adj_term = round(monthly_payment_adj_term, 2)
        total_interest_adj_term = round(total_interest_adj_term, 2)
        total_cost_adj_term = round(total_cost_adj_term, 2)

    return render(request, 'student_loan_calculator.html', {
        'monthly_payment': monthly_payment,
        'total_interest': total_interest,
        'total_cost': total_cost,
        'adjusted_term': adjusted_term,
        'monthly_payment_adj_term': monthly_payment_adj_term,
        'total_interest_adj_term': total_interest_adj_term,
        'total_cost_adj_term': total_cost_adj_term
    })

def car_payment_calcualtor(request):
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

        # Round results
        monthly_payment = round(monthly_payment, 2)
        total_interest = round(total_interest, 2)
        total_cost = round(total_cost, 2)
        adjust_double_initial_payment = round(adjust_double_initial_payment, 2)
        monthly_payment_adj_pay = round(monthly_payment_adj_pay, 2)
        total_interest_adj_pay = round(total_interest_adj_pay, 2)
        total_cost_adj_pay = round(total_cost_adj_pay, 2)

    return render(request, 'car_payment_calculator.html', {
        'monthly_payment': monthly_payment,
        'total_interest': total_interest,
        'total_cost': total_cost,
        'adjust_double_initial_payment': adjust_double_initial_payment,
        'monthly_payment_adj_pay': monthly_payment_adj_pay,
        'total_interest_adj_pay': total_interest_adj_pay,
        'total_cost_adj_pay': total_cost_adj_pay
    })

def loadEntriesFromDB(request, raw_entries):
    previous_entries = []
    for entry in raw_entries:
        input_data = entry.input_data  # Extract JSON data from input_data

        input_data = json.loads(entry.input_data)

        flattened_entry = {
            'usage_date': entry.usage_date,
            'budget_for_date': entry.budget_for_date,
            'fixed_income': input_data.get('fixed_income'),
            'variable_income': input_data.get('variable_income'),
            'one_year_savings_goal': input_data.get('one_year_savings_goal'),
            # Flatten the expenses dictionary
            'housing': input_data.get('expenses', {}).get('housing'),
            'taxes': input_data.get('expenses', {}).get('taxes'),
            'car_payment': input_data.get('expenses', {}).get('car_payment'),
            'internet_phone': input_data.get('expenses', {}).get('internet_phone'),
            'subscriptions': input_data.get('expenses', {}).get('subscriptions'),
            'food': input_data.get('expenses', {}).get('food'),
            'entertainment': input_data.get('expenses', {}).get('entertainment'),
            'personal_items': input_data.get('expenses', {}).get('personal_items'),
            'utilities': input_data.get('expenses', {}).get('utilities'),
            'transportation': input_data.get('expenses', {}).get('transportation'),
            'medical': input_data.get('expenses', {}).get('medical'),
            'misc': input_data.get('expenses', {}).get('misc'),
            # Other data needed for later use
            'usage_id': entry.usage_id
        }
        previous_entries.append(flattened_entry)
    return previous_entries
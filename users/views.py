from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now

from users.models import Payment, Subscription
from .forms import AdvisorForm, ProfileForm, CustomUserCreationForm  # Import the ProfileForm and CustomUserCreationForm
from datetime import timedelta, date  # Add this import

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # The email is already handled in the form's save method
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        # If form is invalid, render the form with errors
        return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    error_message = None
    username = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get('username', '')  # Preserve the username
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
        
        # Create a custom error message based username and password validity     
        error_message = "Invalid login credentials."
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message, 'username': username})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# Profile; Also has subscription status and payment form
@login_required
def profile(request):
    subscription_string = ""

    # Retrieve the logged-in user's profile
    user_profile = request.user.profile

    if not Subscription.objects.filter(user_id=user_profile, start_date__lte=now(), end_date__gte=now()).exists():
        entry = None
        subscription_string = "Not currently subscribed"
    else:
        entry = Subscription.objects.filter(user_id=user_profile, start_date__lte=now(), end_date__gte=now()).get()
        subscription_string = "Subscribed until " + entry.end_date.strftime("%Y-%m-%d")
    
    return render(request, 'profile.html', {
            'subscription_string': subscription_string,
        })
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        advisor_form = AdvisorForm(request.POST, instance=request.user.advisor) if hasattr(request.user, 'advisor') else None
        if form.is_valid() and (not advisor_form or advisor_form.is_valid()):
            profile = form.save(commit=False)
            profile.user.first_name = form.cleaned_data['first_name']
            profile.user.last_name = form.cleaned_data['last_name']
            profile.user.save()
            profile.save()
            if advisor_form:
                advisor_form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })
        advisor_form = AdvisorForm(instance=request.user.advisor) if hasattr(request.user, 'advisor') else None
    return render(request, 'edit_profile.html', {
        'form': form,
        'advisor_form': advisor_form
    })

@login_required
def account_settings(request):

    # gives options to change password and delete account
    return render(request, 'account_settings.html')

@login_required
def delete_account(request):
    if request.method == 'POST' and 'confirm' in request.POST:
        user = request.user
        user.delete()
        return redirect('home')
    return render(request, 'delete_account.html')

@login_required
def payment(request):
    PRICE_PER_DAY = 1.00

    subscription_string = ""
    form_data = {}
    total_price = 0.0

    # Retrieve the logged-in user's profile
    user_profile = request.user.profile
    
    # Check if User is subscribed
    if not Subscription.objects.filter(user_id=user_profile, start_date__lte=now(), end_date__gte=now()).exists():
        entry = None
        subscription_string = "You are currently not subscribed"
    else:
        entry = Subscription.objects.filter(user_id=user_profile, start_date__lte=now(), end_date__gte=now()).get()
        subscription_string = "You are subscribed until: " + entry.end_date.strftime("%Y-%m-%d")

    if request.method == 'POST':
        if request.POST['action'] == 'purchase':
            subscription_days = int(request.POST.get('subscription_days'))
            card_number = str(request.POST.get('card_number'))
            expiration_date = request.POST.get('expiration_date')
            security_code = int(request.POST.get('security_code'))
            country = str(request.POST.get('country'))
            zip_code = int(request.POST.get('zip_code'))

            form_data = {
                "subscription_days": subscription_days,
                "card_number": card_number,
                "expiration_date": expiration_date,
                "security_code": security_code,
                "country": country,
                "zip_code": zip_code
            }

            if entry is not None:
                entry.end_date = entry.end_date + timedelta(days=subscription_days)
                entry.save()
            else:
                new_subscription = Subscription(
                    user_id = user_profile,
                    plan_type = "Standard",
                    start_date = date.today(),
                    end_date = date.today() + timedelta(days=subscription_days),
                    auto_renew = False
                )
                new_subscription.save()
                entry = new_subscription

            total_price = PRICE_PER_DAY * subscription_days

            new_payment = Payment(
                user_id = user_profile,
                amount = total_price,
                payment_method = "Credit Card",
                payment_date = date.today(),
                transaction_id = entry.pk,
                payment_status = "PID"
            )
            new_payment.save()

            # Redirect to prevent duplicate POST requests from making multiple db entries
            return redirect('payment')

    # Shows payment methods and allows to add new ones
    return render(request, 'payment.html', {
        'subscription_string': subscription_string,
        'form_data': form_data,
        'total_price': total_price
    })
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
import random
import string
from django.contrib import messages
from django.core.mail import send_mail  # Add this import
from django.contrib.auth.hashers import check_password  # Add this import
from django.contrib.auth.password_validation import validate_password  # Add this import
from django.core.exceptions import ValidationError  # Add this import

from users.models import Payment, Subscription, OTP  # Add this import
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

    # Display success or error messages from other views
    storage = messages.get_messages(request)
    storage.used = True  # Mark messages as used to clear them # type: ignore

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

# Generate and send a one-time password (OTP) for password reset
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.filter(email=email).first()
            otp_code = ''.join(random.choices(string.digits, k=6))  # Generate a 6-digit OTP
            otp_expiry = now() + timedelta(minutes=10)  # Set OTP expiry time

            # Create a new OTP entry
            OTP.objects.create(
                user=user,
                code=otp_code,
                expires_at=otp_expiry,
                is_used=False
            )

            # Store user ID in session
            request.session['reset_user_id'] = user.pk # type: ignore

            # Send OTP via email (debugging purposes, uncomment in production)
            print(f"Generated OTP for {email}: {otp_code}")
            # send_mail(
            #     'Password Reset OTP',
            #     f'Your OTP for password reset is: {otp_code}',
            #     'noreply@wealthwise.com',
            #     [email],
            #     fail_silently=False,
            # )
            messages.success(request, 'An OTP has been sent to your email.')
            return redirect('verify_otp')  # Redirect to OTP verification page
        except User.DoesNotExist:
            messages.error(request, 'No account found with this email.')
    return render(request, 'forgot_password.html')

def verify_otp(request):
    if request.method == 'POST':
        otp_code = request.POST.get('otp_code')
        try:
            user_id = request.session.get('reset_user_id')
            user = User.objects.get(id=user_id)
            otp_entry = OTP.objects.get(user=user, code=otp_code, is_used=False)
            if otp_entry.expires_at >= now():
                # Mark OTP as used
                otp_entry.is_used = True
                otp_entry.save()
                messages.success(request, 'OTP verified successfully. You can now reset your password.')
                return redirect('reset_password')  # Redirect to password reset page
            else:
                messages.error(request, 'OTP has expired. Please request a new one.')
        except (User.DoesNotExist, OTP.DoesNotExist):
            messages.error(request, 'Invalid OTP. Please try again.')
    return render(request, 'verify_otp.html')

def reset_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            try:
                # Validate the password
                validate_password(new_password)
                
                user_id = request.session.get('reset_user_id')
                user = User.objects.get(id=user_id)
                user.set_password(new_password)
                user.save()
                # Clear session data after successful reset
                del request.session['reset_user_id']
                messages.success(request, 'Password reset successfully. You can now log in.')
                return redirect('login')  # Redirect to login page
            except ValidationError as e:
                # Handle password validation errors
                messages.error(request, ' '.join(e.messages))
            except User.DoesNotExist:
                messages.error(request, 'An error occurred. Please try again.')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    return render(request, 'reset_password.html')

def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user
        if check_password(current_password, user.password):
            if new_password == confirm_password:
                try:
                    # Validate the password
                    validate_password(new_password)
                    
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, 'Password changed successfully.')
                    return redirect('login')  # Redirect to login page after changing password
                except ValidationError as e:
                    # Handle password validation errors
                    messages.error(request, ' '.join(e.messages))
            else:
                messages.error(request, 'New passwords do not match. Please try again.')
        else:
            messages.error(request, 'Current password is incorrect. Please try again.')
            
    return render(request, 'change_password.html')
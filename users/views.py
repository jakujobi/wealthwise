from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User  # Import User model
from .models import Profile  # Import the Profile model
from .forms import ProfileForm, CustomUserCreationForm, AdvisorForm  # Import the ProfileForm, CustomUserCreationForm, and AdvisorForm
import re  # Import the regex module for password validation

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
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# Profile
@login_required
def profile(request):
    return render(request, 'profile.html')

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

# Payment

@login_required
def account_settings(request):
    # gives options to change password and delete account
    return render(request, 'account_settings.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    return render(request, 'delete_account.html')
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Advisor, Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Ensure email is stored in the User model
        if commit:
            user.save()
            # Create a Profile instance without storing the email
            Profile.objects.create(user=user)
        return user

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True, help_text="Required")
    last_name = forms.CharField(required=True, help_text="Required")
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = Profile
        fields = ['email', 'profile_picture', 'first_name', 'last_name', 'phone_number', 'address', 'city', 'state', 'country', 'postal_code']

class AdvisorForm(forms.ModelForm):
    class Meta:
        model = Advisor
        fields = ['bio', 'certifications', 'specialties']
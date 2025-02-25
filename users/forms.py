from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'last_name', 'phone_number', 'phone_number', 'address', 'city', 'state', 'country', 'postal_code']

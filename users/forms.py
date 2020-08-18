"""User forms."""

# Django
from django import forms

class ProfileForm(forms.Form):
    """Profile Form"""

    first_name = forms.CharField(min_length=2, max_length=50, required=True)
    last_name = forms.CharField(min_length=2, max_length=50, required=True)
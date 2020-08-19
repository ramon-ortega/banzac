"""User forms."""

# Django
from django import forms
from django.contrib.auth.models import User

# Models
from users.models import Profile
from transacciones.models import Transaccion

class ProfileForm(forms.Form):
    """Profile Form"""

    first_name = forms.CharField(min_length=2, max_length=50, required=True)
    last_name = forms.CharField(min_length=2, max_length=50, required=True)

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50, required=True)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(),
        required=True
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(),
        required=True
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(),
        required=True
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
        transaccion = Transaccion(transferencia=0, retiro=0, user_id = user.id)
        transaccion.save()

class LoginForm(forms.Form):
    """Login Form"""

    username = forms.CharField(min_length=4, max_length=50, required=True)
    password = forms.CharField(max_length=70, required=True)
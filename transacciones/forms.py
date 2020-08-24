"""Transacciones forms."""

# Django
from django import forms
from django.contrib.auth.models import User

# Models
from users.models import Profile
from transacciones.models import Transaccion

class DepositoForm(forms.Form):
    """Deposito Form."""
    deposito = forms.FloatField(min_value = 1, max_value = 15000);

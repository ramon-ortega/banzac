"""Transacciones views"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


saldo=0

@login_required
def solicitar_saldo(request):
    """Return saldo"""
    return render(request, 'transacciones/saldo.html')

@login_required
def retiro(request):
    return render(request, 'transacciones/retiro.html')

@login_required
def deposito(request):
    return render(request, 'transacciones/deposito.html')

@login_required
def cajero(request):
    return render(request, 'transacciones/base.html')

"""Transacciones views"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Utilities
from django.db.utils import IntegrityError

# Models 
from transacciones.models import Transaccion
from users.models import Profile
from django.contrib.auth.models import User

@login_required
def solicitar_saldo(request):
    """Return saldo"""
    user = User.objects.get(id = request.user.id)
    x = Transaccion.objects.filter(profile_id = request.user.id)
    numero_deposito = len(x)

    saldo_transaccion = Transaccion.objects.filter(profile_id = user.id).latest('created')
    saldo = saldo_transaccion.saldo    

    return render(
        request = request,
        template_name = 'transacciones/saldo.html',
        context = {
            'saldo': saldo,
        }
    )

@login_required
def retiro(request):
    """ Agregamos Retiro """
    user = User.objects.get(id = request.user.id)

    x = Transaccion.objects.filter(profile_id = request.user.id)
    numero_deposito = len(x)
    saldo_transaccion = Transaccion.objects.filter(profile_id = user.id).latest('created')
    saldo = saldo_transaccion.saldo

    if request.method == 'POST':
        retiro = float(request.POST['retiro'])
        if saldo - retiro >= 0:
            saldo = saldo - retiro
            
            transaccion = Transaccion(saldo=saldo, transferencia=0, retiro=retiro, profile_id = user.id, user_id = user.id)
            transaccion.save()

        else:
            saldo = saldo
            return render(request, 'transacciones/retiro.html', { 'error': 'Saldo insuficiente' })

    return render(request, 'transacciones/retiro.html')

@login_required
def deposito(request):
    """Agregamos deposito""" 
    user = User.objects.get(id = request.user.id)

    x = Transaccion.objects.filter(profile_id = request.user.id)
    numero_deposito = len(x)
    saldo_transaccion = Transaccion.objects.filter(profile_id = user.id).latest('created')
    saldo = saldo_transaccion.saldo
    if request.method == 'POST':
        deposito = float(request.POST['deposito'])
        saldo = saldo + deposito

        transaccion = Transaccion(saldo=saldo, transferencia=deposito, retiro=0, profile_id = user.id, user_id = user.id)
        transaccion.save()

    return render(request, 'transacciones/deposito.html')

@login_required
def cajero(request):
    return render(request, 'transacciones/base.html')


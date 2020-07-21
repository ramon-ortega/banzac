"""Transacciones views"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Models 
from transacciones.models import Transaccion
from django.contrib.auth.models import User

@login_required
def solicitar_saldo(request):
    """Return saldo"""

    x = Transaccion.objects.filter(profile_id = request.user.id)
    numero_deposito = len(x)

    saldo_transaccion = Transaccion.objects.get(id = numero_deposito)
    saldo = saldo_transaccion.saldo

    return render(
        request = request,
        template_name = 'transacciones/saldo.html',
        context = {
            'saldo': saldo
        }
    )

@login_required
def retiro(request):
    """ Agregamos Retiro """

    x = Transaccion.objects.filter(profile_id = request.user.id)
    numero_deposito = len(x)
    saldo_transaccion = Transaccion.objects.get(id = numero_deposito)
    saldo = saldo_transaccion.saldo

    if request.method == 'POST':
        retiro = float(request.POST['retiro'])
        saldo = saldo - retiro

    import pdb; pdb.set_trace()


    return render(request, 'transacciones/retiro.html')

@login_required
def deposito(request):
    """Agregamos deposito""" 
    x = Transaccion.objects.filter(profile_id = request.user.id)
    numero_deposito = len(x)

    saldo_transaccion = Transaccion.objects.get(id = numero_deposito)
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

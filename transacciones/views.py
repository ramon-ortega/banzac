"""Transacciones views."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView

# Models 
from transacciones.models import Transaccion
from users.models import Profile
from django.contrib.auth.models import User

class SolicitarSaldoView(ListView, LoginRequiredMixin):
    model = Profile
    template_name = 'transacciones/saldo.html'

@login_required
def retiro(request):
    """ Agregamos Retiro """
    saldo_transaccion = Profile.objects.filter(id = request.user.profile.id).latest('created')
    saldo = saldo_transaccion.saldo

    if request.method == 'POST':
        retiro = float(request.POST['retiro'])
        if saldo - retiro >= 0:
            saldo = saldo - retiro
            
            transaccion = Transaccion(transferencia=0, retiro=retiro, user_id = request.user.id)
            transaccion.save()

            profile = Profile.objects.get(user = request.user)
            profile.saldo = saldo
            profile.save()

        else:
            saldo = saldo
            return render(request, 'transacciones/retiro.html', { 'error': 'Saldo insuficiente' })

    return render(request, 'transacciones/retiro.html')

@login_required
def deposito(request):
    """Agregamos deposito""" 

    saldo_transaccion = Profile.objects.filter(id = request.user.profile.id).latest('created')
    saldo = saldo_transaccion.saldo

    if request.method == 'POST':
        deposito = float(request.POST['deposito'])
        saldo = saldo + deposito

        transaccion = Transaccion(transferencia=deposito, retiro=0, user_id = request.user.id)
        transaccion.save()

        profile = Profile.objects.get(user = request.user)
        profile.saldo = saldo
        profile.save()

    return render(request, 'transacciones/deposito.html')

class CajeroPrincipal(LoginRequiredMixin, TemplateView):
    """Cajero Principal View"""

    template_name = 'transacciones/base.html'


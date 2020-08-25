"""Transacciones views."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView
from django.urls import reverse_lazy, reverse

# Models 
from transacciones.models import Transaccion
from users.models import Profile

# Forms
from transacciones.forms import DepositoForm, RetiroForm

class SolicitarSaldoView(ListView, LoginRequiredMixin):
    model = Profile
    template_name = 'transacciones/saldo.html'

class RetiroView(LoginRequiredMixin, View):
    form_class = RetiroForm
    template_name = 'transacciones/retiro.html'

    def get(self, request, *args, **kwargs):
        form = RetiroForm()
        return render(request, 'transacciones/retiro.html', {'form': form})

    def post(self, request, *args, **kwargs):
        saldo_transaccion = Profile.objects.filter(id = request.user.profile.id).latest('created')
        saldo = saldo_transaccion.saldo
        form = RetiroForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

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

        return render(request, 'transacciones/retiro.html', {'form': form})

class DepositoView(LoginRequiredMixin, View):
    form_class = DepositoForm
    template_name = 'transacciones/deposito.html'

    def get(self, request, *args, **kwargs):
        form = DepositoForm()
        return render(request, 'transacciones/deposito.html', {'form': form})

    def post(self, request, *args, **kwargs):
        saldo_transaccion = Profile.objects.filter(id = request.user.profile.id).latest('created')
        saldo = saldo_transaccion.saldo
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            deposito = float(request.POST['deposito'])
            saldo = saldo + deposito

            transaccion = Transaccion(transferencia=deposito, retiro=0, user_id = request.user.id)
            transaccion.save()

            profile = Profile.objects.get(user = request.user)
            profile.saldo = saldo
            profile.save()

        return render(request, 'transacciones/deposito.html', {'form': form})

class CajeroPrincipal(LoginRequiredMixin, TemplateView):
    """Cajero Principal View"""

    template_name = 'transacciones/base.html'


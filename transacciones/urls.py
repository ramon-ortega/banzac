"""Transacciones URLs."""

#Django 
from django.urls import path
from django.views.generic import TemplateView

# View
from transacciones import views

urlpatterns = [
    path(
        route = '',
        view = views.cajero,
        name = 'feed'
        ),

    path(
        route = 'transacciones/deposito/',
        view = views.deposito,
        name = "deposito"
        ),

    path(
        route = 'transacciones/retiro/',
        view = views.retiro,
        name="retiro"
        ),

    path(
        route = 'transacciones/consultar_saldo/', 
        view = views.solicitar_saldo,
        name="consultar_saldo"
        ),
]
# Transacciones models.


# Django
from django.db import models
from django.contrib.auth.models import User

class Transaccion(models.Model):
    """Transaccion models."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    saldo = models.FloatField(default=0)
    transferencia = models.FloatField(null = True)
    retiro = models.FloatField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return '{}'.format(self.user.username)

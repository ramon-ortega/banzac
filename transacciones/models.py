# Transacciones models.


# Django
from django.db import models
from django.contrib.auth.models import User

class Transaccion(models.Model):
    """Transaccion models."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    saldo = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    transferencia = models.DecimalField(max_digits=6, decimal_places=2)
    retiro = models.DecimalField(max_digits=6, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return '{}'.format(self.user.username)

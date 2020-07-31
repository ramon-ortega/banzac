""" Transacciones admin classes """

# Django
from django.contrib import admin

# Models
from transacciones.models import Transaccion

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    """Transaccion Admin."""
    list_display = ('id', 'user', 'transferencia', 'retiro')
    list_display_links = ('id', 'user')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__username')
    list_filter = ('created', 'modified')

    fieldsets = (
        ('Transaccion',{
            'fields': (
                ('user', 'transferencia', 'retiro'),
            ),
        }),
        ('Metadata',{
            'fields': (
                ('created', 'modified'),
            )
        }),
    )
    readonly_fields = ('created', 'modified')
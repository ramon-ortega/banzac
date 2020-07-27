"""banzac URL Configuration. """

# Django
from django.contrib import admin
from django.urls import path
from users import views as user_views
from transacciones import views as transacciones_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', user_views.login_view, name='home'),

    path('users/login/', user_views.login_view, name="login"),
    path('users/logout/', user_views.logout_view, name="logout"),
    path('users/signup/', user_views.signup, name="signup"),

    path('inicio/', transacciones_views.cajero, name="feed"),
    path('transacciones/deposito/', transacciones_views.deposito, name="deposito"),
    path('transacciones/retiro/', transacciones_views.retiro, name="retiro"),
    path('transacciones/consultar_saldo/', transacciones_views.solicitar_saldo, name="consultar_saldo"),
]

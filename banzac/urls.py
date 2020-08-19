"""banzac URL Configuration. """

# Django
from django.contrib import admin
from django.urls import path, include

from users import views as user_views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('users/', include(('users.urls', 'users'), namespace='users')),

    path('users/login/', user_views.login_view, name="login"),

    path('', include(('transacciones.urls', 'transacciones'), namespace='transacciones')),
]

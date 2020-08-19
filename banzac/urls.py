"""banzac URL Configuration. """

# Django
from django.contrib import admin
from django.urls import path, include

from users import views as user_views
from transacciones import views as transacciones_views

urlpatterns = [

    path('admin/', admin.site.urls),


    path('users/login/', user_views.login_view, name="login"),
    path('users/logout/', user_views.logout_view, name="logout"),
    path('users/signup/', user_views.signup, name="signup"),
    path('users/me/profile/', user_views.update_profile, name="update_profile"),

    path('', include(('transacciones.urls', 'transacciones'), namespace='transacciones')),
]

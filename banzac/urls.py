"""banzac URL Configuration. """

# Django
from django.contrib import admin
from django.urls import path
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('inicio/', user_views.cajero, name="feed"),
    path('users/login/', user_views.login_view, name="login"),
    path('users/logout/', user_views.logout_view, name="logout"),
]

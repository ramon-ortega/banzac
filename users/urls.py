"""Users URLs."""

#Django 
from django.urls import path

# View
from users import views

urlpatterns = [
    path(
        route = 'login/', 
        view = views.LoginView.as_view(), 
        name="login"
        ),

    path(
        route = 'logout/',
        view = views.LogoutView.as_view(), 
        name = "logout"
        ),

    path(
        route = 'signup/', 
        view = views.signup, 
        name = "signup"
        ),

    path(
        route = 'me/profile/',
        view = views.update_profile, 
        name = "update_profile"
        ),

]
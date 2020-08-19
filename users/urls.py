"""Users URLs."""

#Django 
from django.urls import path
from django.views.generic import TemplateView

# View
from users import views

urlpatterns = [


    path(
        route = 'logout/',
        view = views.logout_view, 
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
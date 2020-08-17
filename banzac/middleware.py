"""Platzigram middleware catalog."""

from django.shortcuts import redirect, render
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion middleware
    Para la creacion de supersusers creamos el middleware para que 
    puedan completar los datos.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view
        is called."""
        
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                user = request.user
                if not user.first_name or not user.last_name:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')
        response = self.get_response(request)
        return response
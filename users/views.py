"""Users views."""

# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import View, FormView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

# Error
from django.db.utils import IntegrityError

# Models 
from transacciones.models import Transaccion
from users.models import Profile
from django.contrib.auth.models import User

# Forms
from users.forms import ProfileForm, SignupForm

class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/login.html'

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, View):
    form_class = ProfileForm
    template_name = 'users/update_profile.html'

    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, 'users/update_profile.html', {'form': form})

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = Profile(user=user)
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()

            try:
                profile.save()
                transaccion = Transaccion(transferencia=0, retiro=0, user_id = user.id)
                transaccion.save()
            except IntegrityError:
                render(request, 'users/update_profile.html', {'error': 'Data is the same'})

        return render(request, 'users/update_profile.html', {'form': form})


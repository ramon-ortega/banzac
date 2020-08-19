"""Users views."""

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Error
from django.db.utils import IntegrityError

# Models 
from transacciones.models import Transaccion
from users.models import Profile
from django.contrib.auth.models import User

# Forms
from users.forms import ProfileForm, SignupForm, LoginForm

""" class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('transacciones:feed')
            else:
                return render(request, 'users/login.html', {'error': 'Invalid username and password'})
        else:
            return render(request, 'users/login.html')

        return render(request, 'users/login.html')"""

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('transacciones:feed')
            else:
                return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    else:
        form = LoginForm()

    return render(
        request = request,
        template_name = 'users/login.html',
        context = {
            'form': form
        }
    )

class LogoutView(View):
    """Logout View."""

    def get(self, request):
        logout(request)
        return redirect('users:login')

def signup(request):
    """Signup user."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )

@login_required
def update_profile(request):
    """Update a user's profile view."""
    user = request.user
    profile = Profile(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
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

    else: 
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': user,
            'form': form
        }
    )

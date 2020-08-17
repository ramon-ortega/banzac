"""Users views."""

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Utilities
from django.db.utils import IntegrityError

# Models 
from transacciones.models import Transaccion
from users.models import Profile
from django.contrib.auth.models import User

# Forms
from users.forms import ProfileForm

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout users"""
    logout(request)
    return redirect('login')

def signup(request):
    """Signup user."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Passwords do not match'})
        
        try:
            user = User.objects.create_user(username=username, password=password)
        except 	IntegrityError:
            return render(request, 'users/signup.html', {'error': 'User already exists'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        transaccion = Transaccion(transferencia=0, retiro=0, user_id = user.id)
        transaccion.save()

        return redirect('login')

    return render(request, 'users/signup.html')

def update_profile(request):
    """Update a user's profile view."""
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()

        try:
            profile = Profile(user=user)
            profile.save()

            transaccion = Transaccion(transferencia=0, retiro=0, user_id = user.id)
            transaccion.save()
        except IntegrityError:
            render(request, 'users/update_profile.html', {'error': 'Data is the same'})

    return render(
        request=request,
        template_name='users/update_profile.html',
        )

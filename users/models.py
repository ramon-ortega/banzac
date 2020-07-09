"""Users models."""

# Django
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Profile model
    
    Proxy model that extends the base data with other information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20)
    card_number = models.CharField(max_length=40)
    profile_picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username
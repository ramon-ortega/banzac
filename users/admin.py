"""User admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin."""
    list_display = ('id', 'user', 'phone_number', 'website', 'profile_picture')
    list_display_links = ('id', 'user')
    list_editable = ('phone_number', 'website', 'profile_picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__username', 'phone_number')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    fieldsets = (
        ('Profile',{
            'fields': (
                ('user', 'profile_picture'),
            ),
        }),
        ('Extra Info',{
            'fields': (
                ('phone_number', 'website'),
                ('card_number')
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        }),
    )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    """ Profile inline admin for users"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInline,)

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
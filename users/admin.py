# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Profile

"""Añade modelo para los perfiles a admin"""


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'picture')
    list_display_links = ('pk', 'user',)
    list_editable = ('phone_number', 'picture')

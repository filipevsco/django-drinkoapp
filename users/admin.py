from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .forms import CustomUserCreateForm, CustomUserChangeFotm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeFotm
    model = CustomUser
    list_display = ["first_name", "last_name", "email", "is_staff"]
    fieldsets = {
        (None, {"fields" : ("email": "password")})
        ("Informações Pessoas", {"fields": ("is_active", "is_staff", "is_superuser", "groups")})
    }
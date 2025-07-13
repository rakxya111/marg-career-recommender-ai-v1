from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class CustomUserAdmin(UserAdmin):
    model = Account
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_image',)}),
    )

admin.site.register(Account, CustomUserAdmin)

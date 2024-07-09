from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add any custom admin configurations here
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)

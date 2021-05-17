from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'driver_license_id', 'personal_id', 'address', 'phone',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name',)}),
    )


admin.site.register(Address)
admin.site.register(User, CustomUserAdmin)

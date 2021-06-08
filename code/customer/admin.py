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
    list_display = (
        'first_name', 'last_name', 'email', 'username', 'driver_license_id',
        'personal_id', 'phone', 'is_superuser', 'is_staff', 'is_active',
        'date_joined', 'address',)
    ordering = ('email', 'first_name', 'last_name', 'username', 'date_joined',)
    search_fields = (
        'driver_license_id', 'email', 'phone', 'first_name', 'last_name',
        'username', 'personal_id', 'slug',)
    list_filter = ('is_active', 'is_superuser', 'is_staff')


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'city', 'street', 'house_number', 'flat_number', 'zip_code',)
    ordering = ('city',)
    search_fields = ('slug',)


admin.site.register(Address, AddressAdmin)
admin.site.register(User, CustomUserAdmin)

from django.contrib import admin
from .models import Payment, Service


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('slug', 'payment_method', 'amount', 'is_paid', 'date',)
    list_filter = ('payment_method', 'is_paid',)
    ordering = ('amount', 'date',)
    search_fields = ('slug', 'date',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('slug', 'payment', 'rent_date', 'return_date', 'car',
                    'car_slug', 'customer_username', 'customer_slug')
    ordering = ('rent_date', 'return_date',)
    search_fields = ('slug', 'payment', 'rent_date', 'return_date', 'car_slug',
                     'customer_username', 'customer_slug')

    def car_slug(self, obj):
        return obj.car.slug

    def customer_username(self, obj):
        return obj.customer.username

    def customer_slug(self, obj):
        return obj.customer.slug


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Service, ServiceAdmin)

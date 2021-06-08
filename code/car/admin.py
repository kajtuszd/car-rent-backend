from django.contrib import admin
from .models import Engine, Car


class EngineAdmin(admin.ModelAdmin):
    list_display = ('capacity', 'horsepower', 'engine_type')
    list_filter = ('engine_type',)
    ordering = ('capacity', 'horsepower',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'production_year', 'registration',
                    'status', 'price_per_day', 'fuel_usage', 'max_passengers',
                    'horsepower', 'engine_capacity', 'engine_type',)
    list_filter = ('brand', 'status',)
    ordering = ('fuel_usage', 'price_per_day', 'max_passengers',
                'production_year', 'brand',)
    search_fields = ('brand', 'model', 'registration',)

    def horsepower(self, obj):
        return obj.engine.horsepower

    def engine_capacity(self, obj):
        return obj.engine.capacity

    def engine_type(self, obj):
        return obj.engine.engine_type


admin.site.register(Engine, EngineAdmin)
admin.site.register(Car, CarAdmin)

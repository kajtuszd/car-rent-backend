import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                                            RegexValidator)


class EngineType():
    TYPES = (
        ('PETROL', _('PETROL')),
        ('DIESEL', _('DIESEL')),
        ('HYBRID', _('HYBRID')),
        ('LPG', _('LPG')),
    )


class Engine(models.Model):
    capacity = models.DecimalField(_('Capacity'), default=2.0, max_digits=4, 
                validators=[MaxValueValidator(6.0), MinValueValidator(0.7)],
                                                decimal_places=2, blank=False)
    horsepower = models.IntegerField(_('Horsepower'), blank=False, default=100,
                validators=[MaxValueValidator(1000), MinValueValidator(20)])
    engine_type = models.CharField(_('Engine type'), max_length=20,
                                                    choices=EngineType.TYPES)
    
    class Meta:
        verbose_name = _('engine')
        verbose_name_plural = _('engines')

    def __str__(self):
        return f'{self.engine_type} {self.horsepower}HP {self.capacity}'


def return_current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(return_current_year())(value)


class CarStatus():
    STATUS = (
        ('HIRED', _('HIRED')),
        ('AVAILABLE', _('AVAILABLE')),
        ('IN_REPAIR', _('IN REPAIR'))
    )


class Car(models.Model):
    brand = models.CharField(_('Brand'), max_length=30, blank=False)
    model = models.CharField(_('Model'), max_length=30, blank=False)
    production_year = models.PositiveIntegerField(_('Production year'),
                                                default=return_current_year(),
                                        validators=[MinValueValidator(1990),
                                                    max_value_current_year])
    registration = models.CharField(_('Registration'), 
                validators=[RegexValidator(r'^[A-Z]{2,3}[\s]{1}[0-9A-Z]{5,6}$',
        _("Please enter 2-3 letters, whitespace and 5-6 signs"), 'invalid')],
                            max_length=10, blank=False, unique=True, null=True)
    status = models.CharField(_('Status'), max_length=20,
                                                    choices=CarStatus.STATUS)
    price_per_day = models.DecimalField(_('€ Price per day'), max_digits=5,
            validators=[MaxValueValidator(999.99), MinValueValidator(10.00)],
                                            decimal_places=2, default="50.00")
    fuel_usage = models.DecimalField(_('l/100km fuel usage'), max_digits=3,
            validators=[MaxValueValidator(20.0), MinValueValidator(4.0)],
                                            decimal_places=1, default="7")
    max_passengers = models.IntegerField(_('Max passengers'), default="5",
                    validators=[MaxValueValidator(9), MinValueValidator(3)])
    image = models.ImageField(_('Car image'), null=True, blank=True, upload_to='pics')
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)


    class Meta:
        verbose_name = _('car')
        verbose_name_plural = _('cars')
    
    def __str__(self):
        return f'{self.brand} {self.model} {self.registration}'

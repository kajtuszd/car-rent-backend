from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import validate_decimals


class EngineType():
    TYPES = (
        ('PETROL', _('PETROL')),
        ('DIESEL', _('DIESEL')),
        ('HYBRID', _('HYBRID')),
        ('LPG', _('LPG')),
    )


class Engine(models.Model):
    capacity = models.FloatField(_('Capacity'), default=2.0, blank=False, 
                                                validators=[validate_decimals,
                                                    MaxValueValidator(6.0),
                                                    MinValueValidator(0.7)])
    horsepower = models.IntegerField(_('Horsepower'), blank=False, default=100,
                validators=[MaxValueValidator(1000), MinValueValidator(20)])
    engine_type = models.CharField(_('Engine type'), max_length=20,
                                                    choices=EngineType.TYPES)
    
    class Meta:
        verbose_name = _('engine')
        verbose_name_plural = _('engines')

    def __str__(self):
        return f'{self.engine_type} {self.horsepower}HP {self.capacity}'

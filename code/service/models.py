from .validators import no_future_validator, no_past_validator
from car.models import Car
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from utils.slugify import generate_slug
from django_extensions.db.fields import AutoSlugField


class PaymentMethod():
    METHODS = (
        ('CASH', _('CASH')),
        ('BANK_TRANSFER', _('BANK TRANSFER')),
        ('CREDIT_CARD', _('CREDIT CARD')),
    )


class Payment(models.Model):
    payment_method = models.CharField(_('Payment method'), max_length=20,
                                      choices=PaymentMethod.METHODS)
    amount = models.DecimalField(_('€ Amount due'), max_digits=6,
                                 validators=[MaxValueValidator(5000.00),
                                             MinValueValidator(10.00)],
                                 decimal_places=2, default="50.00")
    is_paid = models.BooleanField(default=False)
    date = models.DateTimeField(_('Payment date'), null=True, blank=True,
                                validators=[no_future_validator],
                                help_text="Enter only if payment was made")
    slug_field = models.CharField(_('Slug'), default=generate_slug,
                                  max_length=7,
                                  unique=True, db_index=True, editable=False)

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __str__(self):
        return f'Payment {self.slug_field}'


class Service(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT)
    rent_date = models.DateTimeField(_('Rent date'), blank=False, null=True,
                                     validators=[no_past_validator])
    return_date = models.DateTimeField(_('Return date'), blank=False, null=True,
                                       validators=[no_past_validator])
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=True,
                            blank=False, unique=False)
    slug_field = models.CharField(_('Slug'), default=generate_slug,
                                  max_length=7,
                                  unique=True, db_index=True, editable=False)

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return f'Service {self.slug_field}'

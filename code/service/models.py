from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from datetime import date


class PaymentMethod():
    METHODS = (
        ('CASH', _('CASH')),
        ('BANK_TRANSFER', _('BANK TRANSFER')),
        ('CREDIT_CARD', _('CREDIT CARD')),
    )


def no_future_validator(payment_date):
    if payment_date.date() > date.today():
        raise ValidationError('Payment cannot be done in the future.')


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
    
    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __str__(self):
        return f'{self.payment_method} {self.amount}€'

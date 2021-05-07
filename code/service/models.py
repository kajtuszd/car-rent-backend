from django.db import models
from django.utils.translation import ugettext_lazy as _


class PaymentMethod():
    METHODS = (
        ('CASH', _('CASH')),
        ('BANK_TRANSFER', _('BANK TRANSFER')),
        ('CREDIT_CARD', _('CREDIT CARD')),
    )


class Payment(models.Model):
    payment_method = models.CharField(_('Payment method'), max_length=20,
                                                choices=PaymentMethod.METHODS)

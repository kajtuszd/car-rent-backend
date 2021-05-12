from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    driver_license_id = models.CharField(_('Driver license ID'), max_length=8,
            validators=[RegexValidator(r'^[A-Z0-9]{8}$', _('Enter your unique ID') )],
            unique=True, blank=False, null=True)
    personal_id = models.CharField(_('Personal ID'), max_length=11,
            validators=[RegexValidator(r'^[0-9]{11}$', _('Enter your unique ID') )],
            unique=True, blank=False, null=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

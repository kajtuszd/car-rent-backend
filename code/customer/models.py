from config.slugify import generate_slug
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (EmailValidator, MaxValueValidator,
                                    MinValueValidator, RegexValidator)


class Address(models.Model):
    city = models.CharField(_('City'), max_length=30, null=True)
    street = models.CharField(_('Street'), max_length=30, null=True)
    house_number = models.IntegerField(_('House number'), null=True,
                                       validators=[MaxValueValidator(1000),
                                                   MinValueValidator(1)])
    flat_number = models.IntegerField(_('Flat number'), null=True, blank=True,
                                      validators=[MaxValueValidator(100),
                                                  MinValueValidator(1)])
    zip_code = models.CharField(_('Zip code'), null=True, max_length=6,
                                validators=[RegexValidator(r'^\d{2}-\d{3}$',
                                                           _('Zip code must '
                                                               'be entered in '
                                                               'the format '
                                                               '12-345.'))])
    slug = models.CharField(_('Slug'), default=generate_slug, unique=True,
                                  max_length=7, db_index=True, editable=False)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return f'{self.slug}'


class User(AbstractUser):
    phone = models.CharField(_('Phone number'), unique=True, null=True,
                            max_length=15, validators=[
            RegexValidator(r'^\+?1?\d{9,15}$', _('Phone number must be '
                                                'entered in the format: '
                                                '123456789 or +48123456789. '
                                                'Up to 15 digits allowed.'))])
    email = models.CharField(_('Email address'), max_length=30, unique=True,
                             validators=[EmailValidator(
                                 message='Please enter valid E-mail address')])
    driver_license_id = models.CharField(_('Driver license ID'), max_length=8,
                                         validators=[
                                             RegexValidator(r'^[A-Z0-9]{8}$',
                                                            _('Enter your '
                                                              'unique ID'))],
                                         unique=True, blank=False, null=True)
    personal_id = models.CharField(_('Personal ID'), max_length=11,
                                   validators=[RegexValidator(r'^[0-9]{11}$',
                                                              _('Enter your '
                                                                'unique ID'))],
                                   unique=True, blank=False, null=True)
    address = models.OneToOneField(Address, on_delete=models.PROTECT,
                                   blank=False, null=True)
    slug = models.CharField(_('Slug'), default=generate_slug, unique=True,
                                  max_length=7, db_index=True, editable=False)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

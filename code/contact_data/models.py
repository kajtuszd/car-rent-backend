from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from utils.slugify import generate_slug


class Contact(models.Model):
    email = models.CharField(_('Email'), max_length=30, unique=True,
                             validators=[EmailValidator(
                                 message='Please enter valid E-mail address')])
    phone = models.CharField(_('Phone number'), unique=True, null=True,
                             max_length=15, validators=[
            RegexValidator(r'^\+?1?\d{9,15}$', _('Phone number must be '
                                                 'entered in the format: '
                                                 '123456789 or +48123456789. '
                                                 'Up to 15 digits allowed.'))])
    slug_field = models.CharField(_('Slug'), default=generate_slug, unique=True,
                                  max_length=7, db_index=True, editable=False)

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

    def __str__(self):
        return f'{self.slug_field}'

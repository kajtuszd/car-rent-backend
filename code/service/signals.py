from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Payment, Service
from django.core.exceptions import ValidationError


@receiver(pre_save, sender=Payment)
def not_paid_validator(instance, **kwargs):
    if instance.is_paid and instance.date is None:
        raise ValidationError('Payment date should be entered.')
    if not instance.is_paid and instance.date:
        raise ValidationError('Please mark the payment as made.')


@receiver(pre_save, sender=Service)
def not_paid_validator(instance, **kwargs):
    if instance.rent_date > instance.return_date:
        raise ValidationError('Return date should be after rent date.')

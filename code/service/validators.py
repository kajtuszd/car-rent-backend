from django.core.exceptions import ValidationError
from datetime import date


def no_future_validator(chosen_date):
    if chosen_date.date() > date.today():
        raise ValidationError('This cannot be done in the future.')


def no_past_validator(chosen_date):
    if chosen_date.date() < date.today():
        raise ValidationError('This cannot be done in the past.')

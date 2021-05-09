from django.utils.crypto import get_random_string
from django.utils.text import slugify


def add_slug(word):
    return slugify(word) + '-' + get_random_string(7)


def generate_slug():
    return get_random_string(7)

from django import template

register = template.Library()

@register.filter(name='length_is')
def length_is(value, arg):
    return len(value) == int(arg)

@register.filter(name='split_phone_numbers')
def split_phone_numbers(phone_numbers):
    """Splits the phone numbers by comma and returns a list."""
    return phone_numbers.split(',')

@register.filter(name='trim')
def trim(value):
    """Trims whitespace from the beginning and end of a string."""
    return value.strip() if isinstance(value, str) else value

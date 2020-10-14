from django.core.exceptions import ValidationError


def starts_with_uppercase(value):
    if value[0] != value[0].upper():
        raise ValidationError('Title must start with uppercase')
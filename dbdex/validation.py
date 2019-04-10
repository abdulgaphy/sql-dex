from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    reg_val = value
    if 'http' in reg_val:
        new_value = reg_val
    else:
        new_value = f'http://{value}'
    try:
        url_validator(new_value)
    except:
        raise ValidationError("input a valid URL")
    return new_value

def validate_dot_com(value):
    if " "  in value:
        raise ValidationError("empty space are not permited")
    return value
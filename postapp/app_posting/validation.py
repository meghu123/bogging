from django.core.validators import ValidationError

def passwordvalidator(value):
    if len(value) <8 or len(value)>20:
        raise ValidationError("Password must be between 8 to 20 character")
    return value


class PasswordValidator(object):
    def __init__(self,min_digits=0,max_digits=0):
        self.min_digits= min_digits
        self.max_digits = max_digits

    def validate(self, value):

        if len(value) < self.min_digits or len(value) > self.max_digits:
            raise ValidationError('The Password must be between 8 to 20 characters')

        if not any(x.islower() for x in value):
            raise ValidationError('The Password must contain at least 1 lower case letter')

        if not any(x.isupper() for x in value):
            raise ValidationError('The Password must contain at least 1 upper case letter')

        if not any(x.isdigit() for x in value):
            raise ValidationError('The Password must contain at least 1 digit')

        if not any(x in '@!*&%$' for x in value):
            raise ValidationError('The Password must contain at least 1 special character')

        return value

    def __call__(self, value):
        return self.validate(value)

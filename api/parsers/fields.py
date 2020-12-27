"""
Basic parsing fields that can be used in multiple places.
"""
from api import errors


class BaseField:
    pass


class ArrayField:
    pass


class BooleanField:
    def __init__(self, required: bool = True):
        self.required = required

    def validate(self, value):
        if value in ["true", "True", "1"]:
            return True
        elif value in ["false", "False", "0"]:
            return False

        if self.required:
            raise errors.FieldError(
                category=errors.FieldError.REQUIRED,
                message="Field is required, expected 'true' or 'false'.")


class StringField:
    def __init__(self, min_length=0, max_length=255, required=True, regex=None):
        pass


class UUIDField:
    def __init__(self):
        pass


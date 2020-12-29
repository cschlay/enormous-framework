"""
Basic parsing fields that can be used in multiple places.
"""
from api import errors


class BaseField:
    def validate(self, value):
        raise NotImplementedError


class ArrayField:
    pass


class BooleanField(BaseField):
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
    """
    Validates the string
    """

    def __init__(self, min_length: int = 0, max_length: int = 255, required: bool = True, regex=None):
        self.min_length: int = min_length
        self.max_length: int = max_length
        self.required: bool = required

    def validate(self, value):
        if self.required:
            if isinstance(value, str):
                if self.min_length <= len(value) <= self.max_length:
                    return value
                raise errors.FieldError(
                    category=errors.FieldError.STRING_LENGTH,
                    message=f""
                )
            raise errors.FieldError(
                category=errors.FieldError.REQUIRED,
                message="Field is required"
            )
        return None


class UUIDField:
    def __init__(self):
        pass


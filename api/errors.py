class HttpNotFound(Exception):
    """Raised when error occurs and 404 response is to be returned."""
    pass


class FieldError(Exception):
    """Generic errors for given fields."""
    REQUIRED = "required"
    STRING_LENGTH = "string_length"

    def __init__(self, category, message):
        self.category = category
        self.message = message

        # TODO: Log

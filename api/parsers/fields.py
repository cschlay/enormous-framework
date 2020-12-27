"""
Basic parsing fields that can be used in multiple places.
"""

class BaseField:
    pass


class StringField:
    def __init__(self, min_length=0, max_length=255, required=True, regex=None):
        pass


class UUIDField:
    def __init__(self):
        pass


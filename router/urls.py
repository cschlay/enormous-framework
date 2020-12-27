from typing import Optional
from urllib.parse import parse_qs, urlparse

from api import errors
from api.parsers.fields import ArrayField


def validate_url_params(params: dict, fields: Optional[dict] = None) -> dict:
    """
    Removes invalid parameters and matches the patterns of query params, it also removes them from list if it
    isn't supposed to accept multiple.

    :param params: the query parameters as string
    :param fields: the fields that should exist or be validated
    :return: the dict of validated parameters
    """
    if fields is None:
        fields = {}

    cleaned_params = {}

    for name, field in fields.items():
        value = params[name]
        if field is not ArrayField:
            value = value[0]
        cleaned_params[name] = field.validate(value)

    return cleaned_params


def validate_resource_id(value: str) -> str:
    """
    Validates the url id and ensures that it cannot be integer to prevent enumeration in urls.

    :param value: the id of resource
    :return: the validated id of a resource
    """
    if value.isdigit():
        raise TypeError
    return value


class URL:
    """
    Keeps all information about the URI.
    """

    def __init__(self, path: str, param_fields: Optional[dict] = None):
        """
        The values are initialized with None and are not parsed unless explicitly accessed by property
        this is for lazy evaluation and improving the speed of url parse by skipping unused parts.

        :param path: The url as given by server.
        """
        url = urlparse(path)
        self.path = url.path.split("/")

        try:
            self.version = int(self.path[1].replace("v", ""))
            self.name = self.path[2]
            self.id = validate_resource_id(self.path[3]) if len(self.path) == 4 else None
            self.params = validate_url_params(parse_qs(url.query), fields=param_fields)
        except (KeyError, TypeError):
            raise errors.HttpNotFound

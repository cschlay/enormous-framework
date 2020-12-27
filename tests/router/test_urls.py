import unittest

from api import errors
from api.parsers import fields
from router import urls


class URLTest(unittest.TestCase):
    """Test the url parsing with valid urls."""

    def test_resource_list(self):
        """URLs like /v1/cars should resolve."""
        url = urls.URL("/v1/tomatoes")
        self.assertEqual(url.version, 1)
        self.assertEqual(url.name, "tomatoes")
        self.assertIsNone(url.id)
        self.assertEqual(url.params, {})

    def test_resource_list_with_query_params(self):
        """URLs like /v1/cars?year=2020 should resolve."""
        url = urls.URL("/v1/tomatoes?expired=true", param_fields={
            "expired": fields.BooleanField()
        })
        self.assertEqual(url.version, 1)
        self.assertEqual(url.name, "tomatoes")
        self.assertIsNone(url.id)
        self.assertEqual(url.params, {
            "expired": True
        })

    def test_resource(self):
        """URLs like /v1/cars/1564rl should resolve."""
        url = urls.URL("/v1/tomatoes/9a908d35-01c8-4734-ac62-3337e5b1c7a2")
        self.assertEqual(url.version, 1)
        self.assertEqual(url.name, "tomatoes")
        self.assertEqual(url.id, "9a908d35-01c8-4734-ac62-3337e5b1c7a2")
        self.assertEqual(url.params, {})

    def test_integer_ids(self):
        """Integer as resource ids should not pass."""
        with self.assertRaises(errors.HttpNotFound):
            urls.URL("/v1/tomatoes/23")

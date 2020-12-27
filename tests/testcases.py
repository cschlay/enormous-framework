import unittest

from starlette.testclient import TestClient

from main import app


class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)


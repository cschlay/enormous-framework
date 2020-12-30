from http import HTTPStatus

from app import user
from tests.testcases import APITestCase


class AuthenticationTest(APITestCase):
    sql_files = [
        "user",
    ]

    def setUp(self) -> None:
        self.username = "karoline"
        self.password = "password123"
        user.create(username=self.username, password=self.password)

    def test_login(self):
        """User that exists should be able to login."""
        res = self.client.post("/v1/login", json={
            "username": self.username,
            "password": self.password
        })
        self.assertEqual(res.status_code, HTTPStatus.OK)
        self.assertIsNotNone(res.json()["token"])

    def test_non_existing_user(self):
        """User that doesn't existing shouldn't be able to login."""
        raise NotImplementedError

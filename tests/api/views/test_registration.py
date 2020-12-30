from http import HTTPStatus

from tests.testcases import APITestCase


class RegistrationTest(APITestCase):
    sql_files = [
        "user",
    ]

    def test_registration(self):
        """Registration with new account should succeed."""

        res = self.client.post("/v1/registration", json={
            "username": "carol",
            "password": "0EP6Xd$UNRrhX$H3"
        })
        self.assertEqual(res.status_code, HTTPStatus.CREATED)
        self.assertEqual(res.json()["username"], "carol")

    def test_username_not_available(self):
        pass


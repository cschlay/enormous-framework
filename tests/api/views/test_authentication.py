from http import HTTPStatus

from tests.testcases import APITestCase


class AuthenticationTest(APITestCase):
    sql_files = [
        "user",
        "authentication"
    ]

    def test_login(self):
        res = self.client.post("/v1/login", json={
            "username": "karoline",
            "password": "password123"
        })
        self.assertEqual(res.status_code, HTTPStatus.OK)

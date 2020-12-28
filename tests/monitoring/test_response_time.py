from http import HTTPStatus

from tests.testcases import APITestCase


class ResponseTimeMeasureTest(APITestCase):
    def test_measure(self):
        """The time between request and response should be measured for any endpoint."""
        res = self.client.get("/v1/tasks")
        self.assertEqual(res.status_code, HTTPStatus.OK)

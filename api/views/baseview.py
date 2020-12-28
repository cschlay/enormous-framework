from api import response
from api.parsers import fields


class BaseView:
    url = {
        "name": fields.StringField(),
        "id": fields.UUIDField()
    }

    params = {

    }

    def __init__(self, method, url,  body):
        self.method = method
        self.url = url
        self.body = body

    def handle_request(self):
        print("handle request")

        return response.Response()


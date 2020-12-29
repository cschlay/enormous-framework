from api import response
from api.views.baseview import BaseView
from api.parsers import fields


class LoginView(BaseView):
    """
    Handles POST /v1/login.
    """

    fields = {
        "username": fields.StringField(max_length=200, required=True),
        "password": fields.StringField(max_length=200, required=True)
    }

    def post(self, data):
        print(data)
        return response.Response()


from http import HTTPStatus

from api import response
from api.views.baseview import BaseView
from api.parsers import fields
from app.authentication.token_authentication import authenticate


class LoginView(BaseView):
    """
    Handles POST /v1/login.
    """

    post_fields = {
        "username": fields.StringField(max_length=200, required=True),
        "password": fields.StringField(max_length=200, required=True)
    }

    def post(self, data):
        """
        Handle the POST methods for /v1/login.

        :param data: contains username and password
        :return: 200 response if success otherwise 400 is returned
        """
        token = authenticate(**data)
        return response.Response(data={"token": token}, status=HTTPStatus.OK)

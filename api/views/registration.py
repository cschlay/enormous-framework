from http import HTTPStatus

from api import response
from api.views.baseview import BaseView
from api.parsers import fields
from app import user


class RegistrationView(BaseView):
    """Handles account creation in POST /v1/registration."""

    post_fields = {
        "username": fields.StringField(max_length=200),
        "password": fields.StringField(min_length=16, max_length=200)
    }

    def post(self, data):
        created_user = user.create(**data)
        return response.Response(data=created_user, status=HTTPStatus.CREATED)

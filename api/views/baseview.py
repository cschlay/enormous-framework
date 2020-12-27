from api.parsers import fields


class BaseView:
    url = {
        "name": fields.StringField(),
        "id": fields.UUIDField()
    }

    params = {

    }

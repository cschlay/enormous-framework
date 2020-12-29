from api import response, errors
from api.parsers import fields
from router.urls import URL


class BaseView:
    url = {
        "name": fields.StringField(),
        "id": fields.UUIDField()
    }

    params = {}
    fields = {}


    def __init__(self, method, url: URL, body):
        self.method = method
        self.url: URL = url
        self.body = body

    def handle_request(self):
        try:
            if self.method == 'POST':
                return self.post(data=self._validate(self.body))

            print("handle request")
        except NotImplementedError:
            # TODO: METHOD NOT ALLOWED ERROR
            return response.Response()

    def post(self, data):
        raise NotImplementedError

    def _validate(self, data: dict):
        """Runs the fields through the validators, always validate all fields."""

        validation_errors: dict = {}
        validated_data: dict = {}

        for name, field in self.fields.items():
            value: any = data.get(name)
            try:
                validated_data[name] = field.validate(value)
            except errors.FieldError as e:
                validation_errors[name] = {

                }

        if not validation_errors:
            return validated_data

        # TODO: raise BadRequest()

from api import response, errors
from api.parsers import fields
from router.urls import URL


class BaseView:
    url = {
        "name": fields.StringField(),
        "id": fields.UUIDField()
    }

    params = {}

    # Common fields that always get checked.
    fields = {}

    # Fields that is checked only for given methods.
    post_fields = {}
    put_fields = {}
    delete_fields = {}


    def __init__(self, method, url: URL, body):
        self.method = method
        self.url: URL = url
        self.body = body

    def handle_request(self):
        try:
            if self.method == 'POST':
                return self.post(data=self._validate(self.body, extra_fields=self.post_fields))

            print("handle request")
        except NotImplementedError:
            # TODO: METHOD NOT ALLOWED ERROR
            return response.Response()

    def post(self, data):
        raise NotImplementedError

    def _validate(self, data: dict, extra_fields: dict):
        """Runs the fields through the validators, always validate all fields."""
        all_fields = {**self.fields, **extra_fields}
        validation_errors: dict = {}
        validated_data: dict = {}

        for name, field in all_fields.items():
            value: any = data.get(name)
            try:
                validated_data[name] = field.validate(value)
            except errors.FieldError as e:
                print(e)
                validation_errors[name] = {

                }

        if not validation_errors:
            return validated_data

        # TODO: raise BadRequest()

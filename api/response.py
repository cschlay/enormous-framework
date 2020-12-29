import json


class Response:
    """Response object that get send to client by main application."""

    def __init__(self, data, status, content_type="application/json"):
        if content_type == "application/json":
            self.body = json.dumps(data).encode()
        self.status = status
        self.content_type = content_type.encode()

    async def send(self, asgi_send):
        await asgi_send({
            "type": "http.response.start",
            "status": self.status,
            "headers": [
                (b"content-type", self.content_type)
            ]
        })
        await asgi_send({
            "type": "http.response.body",
            "body": self.body
        })

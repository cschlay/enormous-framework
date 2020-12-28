from http import HTTPStatus


class Response:
    async def send(self, asgi_send):
        await asgi_send({
            'type': 'http.response.start',
            'status': HTTPStatus.OK,
            "headers": []
        })
        await asgi_send({'type': 'http.response.body'})


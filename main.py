from http import HTTPStatus

from api import errors
from router import urls


async def app(scope, receive, send):
    assert scope["type"] == "http"
    try:
        url, handler = urls.URL(path=scope["path"])

    except errors.HttpNotFound:
        await send({
            'type': 'http.response.start',
            'status': HTTPStatus.NOT_FOUND
        })
        await send({'type': 'http.response.body'})
    except Exception:
        await send({
            'type': 'http.response.start',
            'status': HTTPStatus.INTERNAL_SERVER_ERROR
        })
        await send({'type': 'http.response.body'})

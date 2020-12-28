import timeit
from http import HTTPStatus

from api import errors
from router import router, urls


async def app(scope, receive, send):
    time_start = timeit.default_timer()
    assert scope["type"] == "http"
    try:
        url = urls.URL(path=scope["path"])
        view = router.urls[url.name]
        body = await read_body(receive)
        response = view(method=scope["method"], url=url, body=body).handle_request()
        await response.send(asgi_send=send)
        time_end = timeit.default_timer()
        print(time_end - time_start)
        # TODO: Log the time to database.
    except errors.HttpNotFound:
        await send({
            'type': 'http.response.start',
            'status': HTTPStatus.NOT_FOUND,
            "headers": []
        })
        await send({'type': 'http.response.body'})
    except Exception as e:
        print('error', e)
        await send({
            'type': 'http.response.start',
            'status': HTTPStatus.INTERNAL_SERVER_ERROR,
            "headers": []
        })
        await send({'type': 'http.response.body'})


async def read_body(receive):
    """
    Reads the body from request.

    Snippet taken from: https://www.uvicorn.org/#reading-the-request-body
    """
    body = b''
    more_body = True

    while more_body:
        message = await receive()
        body += message.get('body', b'')
        more_body = message.get('more_body', False)

    return body

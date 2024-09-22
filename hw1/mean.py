import json

from lib import asgi_utils


async def mean_handler(_, receive, send):
    event = await receive()
    if event['type'] != 'http.request':
        return
    try:
        body = event.get('body', b'')
        data = json.loads(body)
        if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
            await asgi_utils.send_json_error(send, 422, 'body must be a list of numbers')
            return
        if not data:
            await asgi_utils.send_json_error(send, 400, 'list must be non empty')
            return
        result = sum(data) / len(data)
        await asgi_utils.send_json(send, {"result": result})
    except json.JSONDecodeError:
        await asgi_utils.send_json_error(send, 422, 'json parsing error')

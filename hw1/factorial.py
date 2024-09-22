import urllib

import math

from lib import asgi_utils

async def factorial_handler(scope, _, send):
    query_params = urllib.parse.parse_qs(scope['query_string'])
    print(query_params)

    if b'n' not in query_params:
        await asgi_utils.send_json_error(send, 422, "required parameter 'n' is missing")
        return

    try:
        n = int(query_params[b'n'][0])
        if n < 0:
            await asgi_utils.send_json_error(send, 400, 'n cannot be negative')
            return
        result = math.factorial(n)
        await asgi_utils.send_json(send, {"result": result})
    except ValueError:
        await asgi_utils.send_json_error(send, 422, 'n must be an integer number')


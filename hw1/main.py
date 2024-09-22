import lib.asgi_utils as asgi_utils
from hw1.factorial import factorial_handler
from hw1.fibonacci import fibonacci_handler
from hw1.mean import mean_handler


async def app(scope, receive, send):
    method = scope["method"]
    path = scope["path"]

    if method == "GET" and path == "/factorial":
        await factorial_handler(scope, receive, send)
    elif method == "GET" and path.startswith("/fibonacci/"):
        await fibonacci_handler(scope, receive, send)
    elif method == "GET" and path == "/mean":
        await mean_handler(scope, receive, send)
    else:
        await asgi_utils.send_json_error(send, 404, '')

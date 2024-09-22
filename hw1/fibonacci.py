import lib.asgi_utils as asgi_utils

async def fibonacci_handler(scope, _, send):
    path = scope["path"]
    try:
        n = int(path.split("/")[-1])
        if n < 0:
            await asgi_utils.send_json_error(send, 400, 'n cannot be negative')
            return
        await asgi_utils.send_json(send, {"result": fibonacci(n)})
    except ValueError:
        await asgi_utils.send_json_error(send, 422, 'n must be integer')


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

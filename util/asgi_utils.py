import json


async def send_json_error(send, status_code, message):
    await send_json(send, {"detail": message}, status_code)


async def send_json(send, data, status_code=200):
    body = json.dumps(data).encode("utf-8")
    await send({
        "type": "http.response.start",
        "status": status_code,
        "headers": [(b"content-type", b"application/json")],
    })
    await send({
        "type": "http.response.body",
        "body": body,
    })

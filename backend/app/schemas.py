def success_response(data, message, meta=None):
    body = {"success": True, "message": message, "data": data}
    if meta is not None:
        body["meta"] = meta
    return body
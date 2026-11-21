from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

def error_response(status_code, code, message, details=None):
    error = {
        "code": code,
        "message": message
    }
    if details is not None:
        error["details"] = details
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": error
        }
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    codes = {
        400: "BAD_REQUEST",
        401: "UNAUTHORIZED",
        403: "FORBIDDEN",
        404: "NOT_FOUND",
        405: "METHOD_NOT_ALLOWED",
        409: "CONFLICT"
    }

    code = codes.get(exc.status_code, "HTTP_ERROR")

    return error_response(
        exc.status_code,
        code,
        str(exc.detail)
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = []

    for error in exc.errors():
        field = ".".join(str(part) for part in error["loc"] if part != "body")
        details.append({
            "field": field,
            "message": error["msg"]
        })
    return error_response(
        400,
        "VALIDATION_ERROR",
        "The request contains invalid or missing fields.",
        details
    )

from rest_framework.exceptions import (
    MethodNotAllowed,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
    Throttled,
)
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        response.data["status_code"] = response.status_code

    if isinstance(exc, Throttled):
        custom_response = {
            "error": "10 messages per hour Maximum reached!",
            "status_code": response.status_code,
        }
        response.data = custom_response

    if isinstance(exc, NotAuthenticated):
        custom_response = {
            "error": "Please login to proceed",
            "status_code": response.status_code,
        }
        response.data = custom_response

    if isinstance(exc, PermissionDenied):
        custom_response = {
            "error": "You are not allowed to do this",
            "status_code": response.status_code,
        }
        response.data = custom_response

    if isinstance(exc, ParseError):
        custom_response = {
            "error": "Your input is not in a correct format",
            "status_code": response.status_code,
        }
        response.data = custom_response

    return response

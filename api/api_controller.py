import json
from flask import Blueprint
from api.api_service import error_handler, pong, get_json

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")


@api_bp.route("/ping")
def pong_controller():
    """
    This function is the controller of the /api/ping route.

    Args:
        - None

    Returns:
        - A string with the message "pong"

    Raises:
        - None
    """
    return pong()


@api_bp.route("/json")
def get_json_controller():
    """
    This function is the controller of the /api/json route.

    Args:
        - Body:
            - data: The variable as plain text that will be returned as a JSON

    Returns:
        - The JSON object

    Example:
        - The vars data shared in the vars.py file

    Raises:
        - BadRequest: If the request is not like the vars.py file
    """
    return get_json()


@api_bp.errorhandler(400)
def bad_request():
    """
    This function is the error handler for the bad request.

    Args:
        - None

    Returns:
        - Bad request message

    Raises:
        - None
    """
    return error_handler(400, "Bad Request")


@api_bp.errorhandler(404)
def not_found():
    """
    This function is the error handler for the not found status.

    Args:
        - None

    Returns:
        - Not found message

    Raises:
        - None
    """
    return error_handler(404, "Not Found")


@api_bp.errorhandler(500)
def internal_server_error():
    """
    This function is the error handler for the internal server errors.

    Args:
        - None

    Returns:
        - Internal server error message

    Raises:
        - None
    """
    return error_handler(500, "Internal Server Error")

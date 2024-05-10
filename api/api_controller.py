import json
from flask import Blueprint
from api.api_service import error_handler, pong, get_json

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")


@api_bp.route("/ping")
def pong_controller():
    return pong()


@api_bp.route("/json")
def get_json_controller():
    return get_json()


@api_bp.errorhandler(400)
def bad_request():
    return error_handler(400, "Bad Request")


@api_bp.errorhandler(404)
def not_found():
    return error_handler(404, "Not Found")


@api_bp.errorhandler(500)
def internal_server_error():
    return error_handler(500, "Internal Server Error")

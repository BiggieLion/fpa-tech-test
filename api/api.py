from flask import Blueprint, jsonify, request

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")


@api_bp.route("/ping")
def pong():
    data = {"status": 200, "message": "pong"}
    return jsonify(data)

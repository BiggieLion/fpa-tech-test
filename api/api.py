from flask import Blueprint, jsonify, request
from .string_cleaner import clean_string
import json

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")


@api_bp.route("/ping")
def pong():
    data = {"status": 200, "message": "pong", "data": {}}
    return jsonify(data)


@api_bp.route("/json")
def get_json():
    raw_text = request.get_data(as_text=True)
    cleaned = clean_string(raw_text)
    json_cleaned = json.loads(cleaned)
    for x in json_cleaned.values():
        print("-- beg -- \n", x, "\n-- end --")

    return jsonify({"status": 200, "message": "ok", "data": json_cleaned})

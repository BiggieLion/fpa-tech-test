import json
from flask import request

from .responses import response_200, response_error
from .string_cleaner import clean_string
from .json_populate import populate_json_response


def error_handler(error, data):
    return response_error(error, data)


def pong():
    return response_200("pong")


def get_json():
    raw_text = request.get_data(as_text=True)
    cleaned = clean_string(raw_text)
    json_cleaned = json.loads(cleaned)
    json_response = populate_json_response(json_cleaned)
    return response_200(json_response)

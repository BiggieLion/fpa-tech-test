from flask import jsonify


def response_200(data):
    return jsonify(
        {"status": 200, "type": "SUCCESS", "action": "CONTINUE", "data": data}
    )


def response_error(error, message):
    return jsonify(
        {
            "status": error,
            "type": "ERROR",
            "action": "CANCEL",
            "data": "Error: " + message,
        }
    )

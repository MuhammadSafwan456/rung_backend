from flask import jsonify, make_response
from __main__ import app


class Error(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, response_code=None, payload=None):
        self.message = message
        if status_code is not None:
            self.status_code = int(status_code)
        self.response_code = response_code
        self.payload = payload

    def to_dict(self):
        data = {
            "message": self.message,
            "status_code": self.status_code,
            "response_code": self.response_code,
            "payload": self.payload
        }
        return data


@app.errorhandler(Error)
def handle_error(error):
    response = error.to_dict()
    status_code = response.pop("status_code")
    response = jsonify(response)
    return make_response(response, status_code)

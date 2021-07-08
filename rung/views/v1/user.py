from flask import request, jsonify, make_response
from __main__ import app
from rung.controllers.user import create_user
import uuid


@app.route("/setup/user", methods=["POST"])
def setup():
    data = request.get_json()
    user_params = {
        "bot": data["bot"],
        "name": data.get("name", None),
        "verified": data["verified"],
        "device_id": data["device_id"]
    }
    user = create_user(user_params)
    print(user)
    return make_response(jsonify(user), 200)

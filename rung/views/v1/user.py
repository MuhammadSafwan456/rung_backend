from flask import request, jsonify, make_response, Blueprint
from rung.controllers.user import create_user

user_api = Blueprint("user_api", __name__, url_prefix='')


@user_api.route("/setup/user", methods=["POST"])
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

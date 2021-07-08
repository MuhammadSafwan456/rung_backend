from flask import request, jsonify, make_response, Blueprint
from rung.controllers.table import join_table

table_api = Blueprint("table_api", __name__, url_prefix='')


@table_api.route("/join/table", methods=["POST"])
def join():
    data = request.get_json()
    user_id = data["user_id"]
    table_capacity = data["table_capacity"]
    join_table(user_id,table_capacity)
    return make_response(jsonify({"ok": "ok"}), 200)

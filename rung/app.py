# import libraries
from flask import Flask, app, jsonify
from rung.views.v1.user import user_api
from rung.views.v1.table import table_api

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False
app.register_blueprint(user_api)
app.register_blueprint(table_api)

if __name__ == '__main__':
    app.run()

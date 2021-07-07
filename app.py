# import libraries
from flask import Flask, app, jsonify


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_SORT_KEYS"] = False

import rung.views.v1.user
if __name__ == '__main__':
    app.run()

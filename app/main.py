from flask import Flask
import json

import app.routes as routes

app = Flask(__name__)

@app.route("/")
def home():
    return json.dumps({"a": 1, "b": "DQA"})
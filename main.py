from flask import Flask
import json

app = Flask("REST API")

@app.route("/")
def home():
    return json.dumps({"a": 1, "b": "DQA"})
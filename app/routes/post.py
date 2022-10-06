from flask import Flask
import json

@app.route("/post")
def post():
    return json.dumps({"post": 1, "title": "DQA"})
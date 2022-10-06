from flask import Flask
import json

@app.route("/post")
def home():
    return json.dumps({"post": 1, "title": "DQA"})
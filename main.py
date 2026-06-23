from flask import Flask, jsonify, request
from flask_cors import CORS
from app.database import init_db

app = Flask(__name__)
CORS(app)

init_db()

@app.route("/")
def index():
    return jsonify('Hello world')

# @app.route("/posts", methods=["GET", "POST"])
# def posts():
#     if(request.method == "GET"):
        
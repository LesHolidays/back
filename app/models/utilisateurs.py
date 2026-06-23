from flask import Flask, jsonify    
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/utilisateurs")
def get_utilisateurs():
    return jsonify({"message": "Liste des utilisateurs"})
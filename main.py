from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify('Hello world')

@app.route("/utilisateurs")
def get_utilisateurs():
    return jsonify({'message': 'Liste des utilisateurs'})

@app.route("/utilisateur/<int:utilisateur_id>")
def get_utilisateur_by_id(utilisateur_id):
    return jsonify({"message": f"Utilisateur avec l'ID {utilisateur_id}"})
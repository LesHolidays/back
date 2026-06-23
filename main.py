from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify('Hello world')

@app.route("/utilisateurs")
def get_utilisateurs():
    return jsonify({'Liste des utilisateurs'})

@app.route("/utilisateur/<int:utilisateur_id>")
def get_utilisateur_by_id(utilisateur_id):
    return jsonify({f"Utilisateur avec l'ID {utilisateur_id}"})

@app.route("/classement")
def get_classement():
    return jsonify({'message': 'Classement des utilisateurs'})

@app.route("/points")
def get_points(points):
    return jsonify({f"Points de l'utilisateur: {points}"})

@app.route("/commentaire")
def get_commentaire(commentaire):
    return jsonify({'message': f"Commentaire: {commentaire}"})

@app.route("/vote", methods=["POST"])
def post_vote():
    return jsonify({'Vote créé'})

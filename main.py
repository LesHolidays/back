from flask import Flask, jsonify, request
from flask_cors import CORS
from app.database import init_db
from app.models.posts import create_post
from app.services.files import allowed_file
import os
from PIL import Image
import io

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

init_db()

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


# @app.route("/login", methods=["POST"])
# def login():
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)
#     if username != "test" or password != "test":
#         return jsonify({"msg": "Mauvais mot de passe"}), 401

#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token)

@app.route("/posts", methods=["GET", "POST"])
def posts():
    if 'file' not in request.files:
        return "Pas d'image envoyée", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Aucun fichier sélectionné', 400
    
    if file and allowed_file(file.filename):
        create_post(file, request.form.get("description"))

    return 'Type de fichier non autorisé', 400
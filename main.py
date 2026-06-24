from datetime import timedelta

from flask import Flask, jsonify, request
from flask_cors import CORS
from app.database import init_db
from app.services import posts_service, files_service, users_service

from flask_jwt_extended import get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
CORS(app)

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=65)
app.config["JWT_SECRET_KEY"] = "super-secret"

jwt = JWTManager(app)

init_db()

@app.route("/")
def index():
    return jsonify('Hello world')

@app.route("/register", methods=["POST"])
def register():
    access_token = users_service.register_user(request.form.get("user_id"), request.form.get("password"))
    return jsonify(access_token=access_token)

@app.route("/login", methods=["POST"])
def login():
    access_token = users_service.login_user(request.form.get("user_id"), request.form.get("password"))
    return jsonify(access_token=access_token)

@app.route("/users")
def get_users():
    users = users_service.get_all_users()
    return jsonify(users)

@app.route("/users/<int:users_id>")
def get_user_by_id(users_id):
    return jsonify({f"Utilisateur avec l'ID {users_id}"})

@app.route("/ranking")
def get_ranking():
    return jsonify({'message': 'Classement des utilisateurs'})

@app.route("/points")
def get_points(points):
    return jsonify({f"Points de l'utilisateur: {points}"})

@app.route("/commentary")
def commentary(commentaire):
    return jsonify({'message': f"Commentaire: {commentaire}"})

@app.route("/vote", methods=["POST"])
def vote():
    return jsonify({'Vote créé'})

@app.route("/posts", methods=["GET", "POST"])
@jwt_required()
def posts():
    if(request.method == "POST"):
        if 'image' not in request.files:
            return "Pas d'image envoyée", 400
        
        file = request.files['image']
        
        if file.filename == '':
            return 'Aucun fichier sélectionné', 400
        
        if file and files_service.allowed_file(file.filename):
            user_id = get_jwt_identity()
            posts_service.create_post(user_id, file, request.form.get("description"))

        return jsonify({"success": True}), 201
    else:
        liste_posts = posts_service.get_posts()
        return jsonify(liste_posts), 200
    
@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    posts_service.delete_post(post_id)
    return jsonify({"success": True}), 200

@app.route("/vote/<int:vote_id>", methods=["DELETE"])
def delete_vote(vote_id):
    vote_service.delete_vote(vote_id)
    return jsonify({"success": True}), 200

@app.route("/commentary/<int:commentary_id>", methods=["DELETE"])
def delete_commentary(commentary_id):
    commentary_service.delete_commentary(commentary_id)
    return jsonify({"success": True}), 200
from flask import Flask, jsonify, request
from flask_cors import CORS
from app.database import init_db
from app.services.posts import create_post
from app.services.files import allowed_file
from app.services.users import register_user, get_all_users

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

init_db()

@app.route("/")
def index():
    return jsonify('Hello world')

@app.route("/register", methods=["POST"])
def register():
    access_token = register_user(request.form.get("user_id"), request.form.get("password"))
    return jsonify(access_token=access_token)

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Mauvais mot de passe"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route("/users")
def get_users():
    users = get_all_users()
    print(users)
    return jsonify(users)

@app.route("/utilisateur/<int:utilisateur_id>")
def get_user_by_id(utilisateur_id):
    return jsonify({f"Utilisateur avec l'ID {utilisateur_id}"})

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
    if 'file' not in request.files:
        return "Pas d'image envoyée", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Aucun fichier sélectionné', 400
    
    if file and allowed_file(file.filename):
        user_id = get_jwt_identity()
        print(user_id)
        create_post(user_id, file, request.form.get("description"))

    return jsonify({"success": True}), 201
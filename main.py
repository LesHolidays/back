from datetime import timedelta

from flask import Flask, jsonify, request
from flask_cors import CORS
from app.database import init_db
from app.services import posts_service, files_service, users_service, commentary_service, vote_service, points_service
from app.errors import NotFoundError, ForbiddenError, ConflictError, BadRequestError, UnauthorizedError

from flask_jwt_extended import get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
CORS(app)

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=65)
app.config["JWT_SECRET_KEY"] = "super-secret"

jwt = JWTManager(app)

init_db()

# ──────────────────────────────────────────────────────────────
# Error handlers globaux
# 
# Ces handlers interceptent les exceptions levées n'importe où 
# dans le code (services, models...) et les transforment en 
# réponses JSON propres avec le bon code HTTP.
#
# Sans ça, Flask renverrait du HTML avec un traceback en mode debug,
# ou une page d'erreur générique en production → inutilisable pour le front.
# ──────────────────────────────────────────────────────────────

@app.errorhandler(BadRequestError)
def handle_bad_request(e):
    return jsonify({"error": str(e)}), 400

@app.errorhandler(UnauthorizedError)
def handle_unauthorized(e):
    return jsonify({"error": str(e)}), 401

@app.errorhandler(ForbiddenError)
def handle_forbidden(e):
    return jsonify({"error": str(e)}), 403

@app.errorhandler(NotFoundError)
def handle_not_found(e):
    return jsonify({"error": str(e)}), 404

@app.errorhandler(ConflictError)
def handle_conflict(e):
    return jsonify({"error": str(e)}), 409

# Handler pour les erreurs inattendues (bugs, erreurs BDD, etc.)
# On ne renvoie PAS le message d'erreur réel pour ne pas exposer
# des détails internes (noms de tables, stack traces...)
@app.errorhandler(Exception)
def handle_unexpected_error(e):
    return jsonify({"error": "Erreur interne du serveur"}), 500

# ──────────────────────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────────────────────

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
    activated = request.args.get("activated") if request.args.get("activated") else False
    users = users_service.get_all_users(activated)
    return jsonify(users)

# feed moins de 24h
@app.route("/posts", methods=["GET", "POST", "DELETE"])
@jwt_required()
def posts():
    if(request.method == "POST"):
        if 'image' not in request.files:
            raise BadRequestError("Pas d'image envoyée")
        
        file = request.files['image']
        
        if file.filename == '':
            raise BadRequestError("Aucun fichier sélectionné")
        
        if not (file and files_service.allowed_file(file.filename)):
            raise BadRequestError("Format de fichier non autorisé (png, jpg, jpeg, gif)")

        user_id = get_jwt_identity()
        points_added = posts_service.create_post(user_id, file, request.form.get("description"))

        return jsonify({"success": True, "points_added": points_added}), 201
    elif(request.method == "GET"):
        user_id = int(get_jwt_identity())
        page = int(request.args.get("page", 1))
        result = posts_service.get_principal_feed(user_id, page)
        return jsonify(result), 200
    else:
        user_id = get_jwt_identity()
        post_id = request.args.get("postId")
        points_removed = posts_service.delete_post(user_id, post_id)
        return jsonify({"success": True, "points_removed": points_removed}), 200
    
# archives
@app.route("/archives", methods=["GET"])
@jwt_required()
def get_archives_feed():
    user_id = int(get_jwt_identity())
    page = int(request.args.get("page", 1))
    result = posts_service.get_archives_feed(user_id, page)
    return jsonify(result), 200

# user feed
@app.route("/user_feed", methods=["GET"])
@jwt_required()
def get_user_feed():
    user_id = get_jwt_identity()
    page = int(request.args.get("page", 1))
    result = posts_service.get_user_feed(user_id, page)
    return jsonify(result), 200

@app.route("/posts/<int:post_id>", methods=["PUT"])
@jwt_required()
def update_description(post_id):
    user_id = get_jwt_identity()
    # request.json vaut None si le body n'est pas du JSON valide
    # (ou si le Content-Type n'est pas application/json)
    if not request.json or "description" not in request.json:
        raise BadRequestError("La description est requise")
    description = request.json.get("description")
    posts_service.update_description(user_id, post_id, description)
    return jsonify({"success": True}), 200

@app.route("/ranking")
def ranking():
    ranking = points_service.get_ranking()
    return jsonify(ranking)

@app.route("/vote", methods=["POST"])
@jwt_required()
def vote():
    user_id = get_jwt_identity()
    voted_user_id = request.form.get("votedUserId")
    post_id = request.form.get("postId")
    vote_response = vote_service.submit_vote(user_id, voted_user_id, post_id)
    return jsonify(vote_response)

@app.route("/commentaries", methods=["POST", "GET", "DELETE"])
@jwt_required()
def commentaries():
    if(request.method == "GET"):
        post_id = request.args.get("postId")
        commentaries = commentary_service.get_commentaries(post_id)
        return jsonify(commentaries)
    elif(request.method == "POST"):
        post_id = request.form.get("postId")
        message = request.form.get("message")
        user_id = get_jwt_identity()
        commentary_service.create_commentary(message, post_id, user_id)
        return jsonify({"success": True}), 201
    else:
        commentary_id = request.args.get("commentaryId")
        user_id = get_jwt_identity()
        commentary_service.delete_commentary(commentary_id, user_id)
        return jsonify({"success": True}), 200

@app.route("/votes")
def votes():
    post_id = request.args.get("postId")
    post_creator_id = request.args.get("postCreatorId")
    users_who_guessed = vote_service.get_who_guessed(post_id, post_creator_id)
    return jsonify(users_who_guessed)
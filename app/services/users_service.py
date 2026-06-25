from flask_jwt_extended import create_access_token
import bcrypt
from ..models import users_model
from ..errors import NotFoundError, ConflictError, BadRequestError, UnauthorizedError

def register_user(user_id, password):
    # Validation des paramètres d'entrée
    # On vérifie AVANT d'aller en BDD pour éviter des requêtes inutiles
    if not user_id or not password:
        raise BadRequestError("L'identifiant et le mot de passe sont requis")

    # On récupère l'user pour vérifier qu'il existe dans la liste de la classe
    user = users_model.get_user_by_id(user_id)
    if not user:
        raise NotFoundError("Utilisateur introuvable")

    # 409 Conflict = "la ressource existe déjà dans cet état"
    # C'est plus précis qu'un 400 car le problème n'est pas la requête, 
    # c'est que le compte est déjà activé
    if user["activated"]:
        raise ConflictError("Compte déjà créé")

    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hashe = bcrypt.hashpw(password_bytes, salt)

    users_model.activate_user(user_id, password_hashe)
    return create_access_token(identity=user_id)

def login_user(user_id, input_password):
    if not user_id or not input_password:
        raise BadRequestError("L'identifiant et le mot de passe sont requis")

    user = users_model.get_user_by_id(user_id)
    
    # 401 Unauthorized = "je ne sais pas qui tu es"
    # On utilise le même message vague pour les 2 cas (user inexistant / pas activé)
    # pour ne pas donner d'indice à un attaquant
    if not user or not user["activated"]:
        raise UnauthorizedError("Identifiants invalides")

    hashed_password = user["password"].encode('utf-8')
    input_password_bytes = input_password.encode('utf-8')
    
    if not bcrypt.checkpw(input_password_bytes, hashed_password):
        raise UnauthorizedError("Identifiants invalides")
    
    return create_access_token(identity=user_id)

def get_all_users(activated = False):
    return users_model.get_users(activated)
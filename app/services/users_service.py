from flask_jwt_extended import create_access_token
import bcrypt
from ..models import users_model

def register_user(user_id, password):
    user_already_activated = users_model.get_user_by_id(user_id)["activated"]

    if(user_already_activated):
        raise Exception("Compte déjà créé")

    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hashe = bcrypt.hashpw(password_bytes, salt)

    try:
        users_model.activate_user(user_id, password_hashe)
        return create_access_token(identity=user_id)
    except:
        raise

def login_user(user_id, input_password):
    hashed_password = users_model.get_user_by_id(user_id)["password"].encode('utf-8')
    input_password_bytes = input_password.encode('utf-8')
    if(bcrypt.checkpw(input_password_bytes, hashed_password)):
        return create_access_token(identity=user_id)
    else:
        raise Exception("Mauvais mot de passe")

def get_all_users(activated = False):
    return users_model.get_users(activated)
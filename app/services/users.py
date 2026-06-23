from flask_jwt_extended import create_access_token
import bcrypt
from ..models.users import activate_user, get_user_by_id, get_users

def register_user(user_id, password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hashe = bcrypt.hashpw(password_bytes, salt)

    try:
        activate_user(user_id, password_hashe)
        return create_access_token(identity=user_id)
    except:
        raise

def login(user_id, input_password):
    hashed_password = get_user_by_id(user_id).password
    input_password_bytes = input_password.encode('utf-8')
    if(bcrypt.checkpw(input_password_bytes, hashed_password)):
        return create_access_token(identity=user_id)
    else:
        pass

def get_all_users():
    return get_users()
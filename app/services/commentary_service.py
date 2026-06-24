
from ..models import commentary_model

def create_commentary(message, post_id, user_id):
    commentary_model.create_commentary(message, post_id, user_id)

def delete_commentary(commentary_id, user_id):
    commentary_model.delete_commentary(commentary_id, user_id)

def update_commentary(commentary_id, message):
    commentary_model.update_commentary(commentary_id, message)

def get_commentaries(post_id):
    return commentary_model.get_commentaries(post_id)
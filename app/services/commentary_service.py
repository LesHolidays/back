
from ..models import commentary_model, posts_model
from ..errors import NotFoundError, ForbiddenError, BadRequestError
from datetime import datetime, timedelta

def create_commentary(message, post_id, user_id):
    if not message or not post_id:
        raise BadRequestError("Le message et l'identifiant du post sont requis")

    # On vérifie que le post existe ET qu'il a moins de 24h
    # Pourquoi ici et pas dans le model ? Parce que c'est de la logique métier :
    # "on ne peut commenter que les posts récents" est une règle de l'app,
    # pas une contrainte de la base de données
    post = posts_model.get_post_by_id(post_id)
    if not post:
        raise NotFoundError("Post introuvable")

    creation_date = datetime.strptime(post["creation_date"], '%Y-%m-%d %H:%M:%S')
    if datetime.now() - creation_date > timedelta(hours=24):
        raise BadRequestError("Impossible de commenter un post de plus de 24 heures")

    commentary_model.create_commentary(message, post_id, user_id)

def delete_commentary(commentary_id, user_id):
    if not commentary_id:
        raise BadRequestError("L'identifiant du commentaire est requis")

    # Même pattern que pour les posts :
    # 1. Le commentaire existe ? → 404
    # 2. C'est le tien ? → 403
    # 3. OK, on supprime
    commentary = commentary_model.get_commentary_by_id(commentary_id)
    if not commentary:
        raise NotFoundError("Commentaire introuvable")

    if commentary["user_id"] != int(user_id):
        raise ForbiddenError("Vous ne pouvez supprimer que vos propres commentaires")

    commentary_model.delete_commentary(commentary_id)

def update_commentary(commentary_id, message):
    commentary_model.update_commentary(commentary_id, message)

def get_commentaries(post_id):
    if not post_id:
        raise BadRequestError("L'identifiant du post est requis")
    return commentary_model.get_commentaries(post_id)
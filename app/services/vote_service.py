from ..models import vote_model, posts_model, points_model
from ..errors import NotFoundError, BadRequestError
from datetime import datetime, timedelta

def submit_vote(user_id, voted_user_id, post_id):
    if not voted_user_id or not post_id:
        raise BadRequestError("L'identifiant du post et de l'utilisateur voté sont requis")

    # Vérifier que le post existe avant de voter dessus
    post = posts_model.get_post_by_id(post_id)
    if not post:
        raise NotFoundError("Post introuvable")

    post_date = datetime.strptime(post["creation_date"], '%Y-%m-%d %H:%M:%S')
    if datetime.now() - post_date > timedelta(hours=24):
        raise BadRequestError("Il n'est plus possible de voter pour un post de plus de 24 heures")

    post_creator = posts_model.get_post_creator(post_id)
    if not post_creator:
        raise NotFoundError("Créateur introuvable")

    nb_votes_remaining = 5 - vote_model.get_nb_vote_on_post(post_id, user_id)
    if(nb_votes_remaining <= 0):
        raise BadRequestError("Plus de vote disponible pour ce post")

    vote_model.create_vote(post_id, user_id, voted_user_id)

    if(int(voted_user_id) == int(post_creator["user_id"])):
        points_added = nb_votes_remaining
        points_model.add_points(points_added, user_id)
        return {
            "guessed": True,
            "remaining": nb_votes_remaining,
            "creator": post_creator["first_name"] + " " + post_creator["last_name"],
            "points_added": points_added
        }
    if(nb_votes_remaining > 1):
        return {
            "guessed": False,
            "remaining": nb_votes_remaining - 1,
            "points_added": 0
        }
    return {
            "guessed": False,
            "remaining": 0,
            "creator": post_creator["first_name"] + " " + post_creator["last_name"],
            "points_added": 0
        }
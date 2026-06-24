from ..models import vote_model, posts_model, points_model

def submit_vote(user_id, voted_user_id, post_id):
    nb_votes_remaining = 5 - vote_model.get_nb_vote_on_post(post_id, user_id)
    if(nb_votes_remaining <= 0):
        raise Exception("Plus de vote dispo")
    post_creator = posts_model.get_post_creator(post_id)
    vote_model.create_vote(post_id, user_id, voted_user_id)

    if(int(voted_user_id) == int(post_creator["user_id"])):
        points_model.add_points(nb_votes_remaining, user_id)
        return {
            "guessed": True,
            "remaining": nb_votes_remaining,
            "creator": post_creator["first_name"] + " " + post_creator["last_name"]
        }
    if(nb_votes_remaining > 1):
        return {
            "guessed": False,
            "remaining": nb_votes_remaining - 1
        }
    return {
            "guessed": False,
            "remaining": 0,
            "creator": post_creator["first_name"] + " " + post_creator["last_name"]
        }
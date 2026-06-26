import base64
from ..models import posts_model, points_model, vote_model
from ..errors import NotFoundError, ForbiddenError, BadRequestError, ConflictError
from PIL import Image
import io
import json
import urllib.request
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

POINTS_CREATE_POST = 3
POINTS_DELETE_POST = -3

def create_post(user_id, image, description):
    # Vérifier qu'il n'a pas déjà posté dans les 24 dernières heures
    # On fait cette vérif AVANT de traiter l'image pour ne pas gaspiller 
    # du temps de traitement si on va refuser de toute façon
    if posts_model.has_recent_post(user_id):
        raise ConflictError("Vous avez déjà publié un post dans les dernières 24 heures")

    img = Image.open(image.stream)
    img_format = img.format if img.format else 'PNG'
    img.thumbnail((800, 800))
    memoire_tampon = io.BytesIO()
    img.save(memoire_tampon, format=img_format)
    blob = memoire_tampon.getvalue()
    posts_model.create_post(user_id, blob, description)
    send_notif()
    points_model.add_points(POINTS_CREATE_POST, user_id)
    return POINTS_CREATE_POST

def delete_post(user_id, post_id):
    if not post_id:
        raise BadRequestError("L'identifiant du post est requis")

    # Étape 1 : le post existe-t-il ?
    # Si on ne faisait pas cette vérification, on supprimerait "0 lignes" 
    # silencieusement et l'utilisateur ne saurait pas pourquoi ça n'a pas marché
    post = posts_model.get_post_by_id(post_id)
    if not post:
        raise NotFoundError("Post introuvable")

    # Étape 2 : est-ce que c'est TON post ?
    # C'est ici qu'on remplace le "AND user_id=?" du SQL.
    # Avantage : on peut renvoyer 403 (interdit) au lieu de 404 (introuvable)
    # L'utilisateur sait que le post existe mais qu'il n'a pas le droit de le supprimer
    if post["user_id"] != int(user_id):
        raise ForbiddenError("Vous ne pouvez supprimer que vos propres posts")

    successful_voters = vote_model.get_successful_voters(post_id, post["user_id"])
    for voter in successful_voters:
        points_model.add_points(-voter["points_to_remove"], voter["user_id"])

    posts_model.delete_post(post_id)
    points_model.add_points(POINTS_DELETE_POST, user_id)
    return POINTS_DELETE_POST

def update_description(user_id, post_id, description):
    post = posts_model.get_post_by_id(post_id)
    if not post:
        raise NotFoundError("Post introuvable")

    if post["user_id"] != int(user_id):
        raise ForbiddenError("Vous ne pouvez modifier que vos propres posts")

    posts_model.update_description(post_id, description)

def send_notif():
    try:
        load_dotenv()
        url = os.getenv("WEBHOOK_URL")
        data = json.dumps({"content": "Nouvelle photo sur [Holidays](https://holidays.super-sympa.fr) !"}).encode()
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "HolidaysBot/1.0"
        }
        urllib.request.urlopen(urllib.request.Request(url, data, headers))
    except:
        pass

def format_posts(rows):
    posts = []
    for row in rows:
        post = dict(row)
        blob_data = post["image"]
        
        if isinstance(blob_data, str):
            if blob_data.startswith("b'") or blob_data.startswith('b"'):
                import ast
                blob_data = ast.literal_eval(blob_data)
            else:
                blob_data = blob_data.encode('utf-8')
        
        base64_data = base64.b64encode(blob_data).decode('utf-8')
        mime_type = "image/png" if b"PNG" in blob_data[:10] else "image/jpeg"
        post["image"] = f"data:{mime_type};base64,{base64_data}"

        posts.append(post)
    return posts

def get_principal_feed(user_id, page=1, limit=10):
    offset = (page - 1) * limit
    rows = posts_model.get_principal_feed(user_id, limit=limit, offset=offset)
    total = posts_model.count_principal_feed(user_id)
    posts = format_posts(rows)
    return {"posts": posts, "has_more": (offset + len(posts)) < total}

def get_archives_feed(user_id, page=1, limit=10):
    offset = (page - 1) * limit
    rows = posts_model.get_archives_feed(user_id, limit=limit, offset=offset)
    total = posts_model.count_archives_feed(user_id)
    posts = format_posts(rows)
    return {"posts": posts, "has_more": (offset + len(posts)) < total}

def get_user_feed(user_id, page=1, limit=10):
    offset = (page - 1) * limit
    rows = posts_model.get_user_feed(user_id, limit=limit, offset=offset)
    total = posts_model.count_user_feed(user_id)
    posts = format_posts(rows)
    return {"posts": posts, "has_more": (offset + len(posts)) < total}
from ..database import get_db
from datetime import datetime
from datetime import timedelta
from sqlite3 import Binary

def create_post(user_id, blob, description):
    conn = get_db()
    cur = conn.cursor()
    try:
        creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(
            'INSERT INTO Post (user_id, image, description, creation_date) VALUES (?, ?, ?, ?)',
            (user_id, Binary(blob), description, creation_date)
        )
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

# Vérifie si l'utilisateur a déjà un post dans les dernières 24h
# On compte les posts récents plutôt que de chercher le dernier,
# parce que count(*) renvoie toujours un résultat (0 ou plus), 
# c'est plus simple à gérer qu'un fetchone qui peut renvoyer None
def has_recent_post(user_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        stopdate = (datetime.now() - timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("SELECT count(*) count FROM Post WHERE user_id=? AND creation_date >= ?", (user_id, stopdate))
        result = cur.fetchone()
        return result["count"] > 0
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def get_all_posts():
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT post_id, image, description FROM Post")
        posts = cur.fetchall()
        return posts
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()

def get_principal_feed(user_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        stopdate = (datetime.now() - timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(
            """
            SELECT DISTINCT p.post_id, p.image, p.description, p.creation_date, u.user_id 
            FROM Post p
            JOIN User u ON p.user_id = u.user_id
            LEFT JOIN Vote v ON p.post_id = v.post_id
            WHERE p.creation_date >= ?
            AND p.user_id != ?
            AND (SELECT count(*) FROM Vote WHERE post_id=p.post_id AND user_id=? AND voted_user_id=p.user_id) <= 0
            AND (SELECT count(*) FROM Vote WHERE post_id=p.post_id AND user_id=?) <= 4
            ORDER BY p.creation_date DESC
            """,
            (stopdate, user_id, user_id, user_id)
        )
        feed = cur.fetchall()
        return feed
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def get_archives_feed(user_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        stopdate = (datetime.now() - timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(
            """
            SELECT DISTINCT p.post_id, u.first_name, u.last_name,p.image, p.description, p.creation_date
            FROM Post p
            JOIN User u ON p.user_id = u.user_id
            LEFT JOIN Vote v ON p.post_id = v.post_id
            WHERE p.creation_date < ?
            OR (SELECT count(*) FROM Vote WHERE post_id=p.post_id AND user_id=? AND voted_user_id=p.user_id) > 0
            OR (SELECT count(*) FROM Vote WHERE post_id=p.post_id AND user_id=?) > 4
            ORDER BY p.creation_date DESC
            """,
            (stopdate,user_id, user_id)
        )
        archives = cur.fetchall()
        return archives
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def get_user_feed(user_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            SELECT DISTINCT p.post_id, u.first_name, u.last_name,p.image, p.description, p.creation_date
            FROM Post p
            JOIN User u ON p.user_id = u.user_id
            WHERE p.user_id = ?
            ORDER BY p.creation_date DESC
            """,
            (user_id,)
        )
        user_feed = cur.fetchall()
        return user_feed
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def get_post_by_id(post_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM Post WHERE post_id=?", (post_id,))
        post = cur.fetchone()
        return post
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def delete_post(post_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM Post WHERE post_id=?", (post_id,))
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def update_description(post_id, description):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("UPDATE Post SET description = ? WHERE post_id = ?", (description, post_id))
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()


def get_post_creator(post_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT u.user_id, u.first_name, u.last_name FROM Post p JOIN User u ON p.user_id=u.user_id WHERE p.post_id=?", (post_id,))
        post = cur.fetchone()
        return post
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()
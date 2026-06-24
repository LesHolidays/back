import base64

from ..database import get_db
from datetime import datetime
from datetime import timedelta
from sqlite3 import Binary

def create_post(user_id, blob, description):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO Post (user_id, image, description, creation_date) VALUES (?, ?, ?, ?)', (user_id, Binary(blob), description, datetime.now()))
        conn.commit()
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


def get_principal_feed():
    conn = get_db()
    cur = conn.cursor()

    try:
        stopdate = (datetime.now() - timedelta(hours=24))
        cur.execute(
            "SELECT post_id, image, description, creation_date FROM Post WHERE creation_date >= ? ORDER BY creation_date DESC",
            (stopdate,)
        )
        feed = cur.fetchall()
        return feed
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def get_archives_feed():
    conn = get_db()
    cur = conn.cursor()

    try:
        stopdate = (datetime.now() - timedelta(hours=24))
        cur.execute(
            """
            SELECT p.post_id, u.first_name, u.last_name,p.image, p.description, p.creation_date
            FROM Post p
            JOIN User u ON p.user_id = u.user_id
            WHERE p.creation_date < ? 
            ORDER BY p.creation_date DESC
            """,
            (stopdate,)
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
            SELECT p.post_id, u.first_name, u.last_name,p.image, p.description, p.creation_date
            FROM Post p
            JOIN User u ON p.user_id = u.user_id
            WHERE p.user_id = ?
            ORDER BY p.creation_date DESC
            """,
            (user_id, datetime.now(),)
        )
        user_feed = cur.fetchall()
        return user_feed
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def delete_post(post_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM Post WHERE post_id = ?", (post_id,))
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
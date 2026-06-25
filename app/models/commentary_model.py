from ..database import get_db
from datetime import datetime

def create_commentary(message, post_id, user_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Commentary (commentary, post_id, user_id, creation_date) VALUES (?,?,?,?)", (message, post_id, user_id, datetime.now()))
        conn.commit()
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()

def get_commentary_by_id(commentary_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM Commentary WHERE commentary_id=?", (commentary_id,))
        commentary = cur.fetchone()
        return commentary
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def delete_commentary(commentary_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM Commentary WHERE commentary_id=?", (commentary_id,))
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def update_commentary(commentary_id, message):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("UPDATE commentary SET message = ? WHERE commentary_id = ?", (message, commentary_id))
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def get_commentaries(post_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT c.commentary_id, c.commentary, u.first_name, u.last_name, c.user_id FROM Commentary c JOIN User u ON u.user_id=c.user_id WHERE c.post_id=?", (post_id,))
        commentaries = cur.fetchall()
        return commentaries
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()
from ..database import get_db

def create_commentary(message, post_id, user_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Post (messsage, post_id, user_id) VALUES (?,?,?)", (message, post_id, user_id))
        conn.commit()
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()

def delete_commentary(commentary_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM commentary WHERE commentary_id = ?", (commentary_id,))
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
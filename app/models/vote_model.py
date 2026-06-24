from ..database import get_db

def vote(vote, post_id, user_id, voted_user_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Post (vote, post_id, user_id, voted_user_id) VALUES (?, ?, ?, ?)", (vote, post_id, user_id, voted_user_id))
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def delete_vote(vote_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM vote WHERE vote_id = ?", (vote_id,))
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

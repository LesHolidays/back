from ..database import get_db

def create_vote(post_id, user_id, voted_user_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Vote (post_id, user_id, voted_user_id) VALUES (?, ?, ?)", (post_id, user_id, voted_user_id))
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


def get_nb_vote_on_post(post_id, user_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT count(*) count FROM Vote WHERE post_id=? AND user_id=?", (post_id, user_id))
        result = cur.fetchone()
        return result["count"]
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

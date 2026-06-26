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

def get_successful_voters(post_id, post_creator_id):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT user_id, 6 - COUNT(*) as points_to_remove
            FROM Vote
            WHERE post_id = ?
            GROUP BY user_id
            HAVING SUM(CASE WHEN voted_user_id = ? THEN 1 ELSE 0 END) > 0
        """, (post_id, post_creator_id))
        result = cur.fetchall()
        return result
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def get_who_guessed(post_id, post_creator_id):
    conn = get_db()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT u.first_name, u.last_name FROM Vote v JOIN User u ON v.user_id = u.user_id WHERE post_id = ? AND voted_user_id = ?", (post_id, post_creator_id))
        result = cur.fetchall()
        return result
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()
        
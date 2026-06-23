from ..database import get_db

def vote(vote, id_post, id_utilisateur, id_pour_qui_a_vote):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO post (vote, id_post, id_utilisateur, id_pour_qui_a_vote) VALUES (?, ?, ?, ?)", (vote, id_post, id_utilisateur, id_pour_qui_a_vote))
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()
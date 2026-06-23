from ..database import get_db

def get_commentaire(commentaire,id_post,id_utilisateur):
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO post(commentaire,id_post,id_utilisateur) VALUES (?,?,?)", (commentaire,id_post,id_utilisateur))
        commentaire = cur.fetchall()
        return commentaire
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()

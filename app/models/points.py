from ..database import get_db

def points(x,id_utilisateur):
    conn = get_db()
    cur = conn.cursor()
    
    try:
        cur.execute("UPDATE utilisateur SET points=points+x WHERE id_utilisateur = ?", (x, id_utilisateur))
        points = cur.fetchall()
        return points
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()
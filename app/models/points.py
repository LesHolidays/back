from ..database import get_db

def points(x):
    conn = get_db()
    cur = conn.cursor()
    
    try:
        cur.execute("UPDATE utilisateur SET points=points+x", (x,))
        points = cur.fetchall()
        return points
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()
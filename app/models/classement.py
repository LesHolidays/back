from ..database import get_db

def create_classement():
    conn = get_db()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT points FROM utilisateur ORDER BY points DESC")
        classement = cur.fetchall()
        return classement
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()
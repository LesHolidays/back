from ..database import get_db

def get_ranking():
    conn = get_db()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT points FROM User ORDER BY points DESC")
        ranking = cur.fetchall()
        return ranking
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()
from ..database import get_db

def add_points(x, user_id):
    conn = get_db()
    cur = conn.cursor()
    
    try:
        cur.execute("UPDATE User SET points=points+? WHERE user_id=?", (x, user_id))
        conn.commit()
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()

def get_ranking():
    conn = get_db()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT user_id, first_name, last_name, points FROM User ORDER BY points DESC")
        ranking = cur.fetchall()
        return ranking
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()
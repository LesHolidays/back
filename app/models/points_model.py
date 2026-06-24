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
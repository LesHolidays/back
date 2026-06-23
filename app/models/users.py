from ..database import get_db

def get_users():
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT user_id, last_name, first_name, activated FROM User")
        users = cur.fetchall()
        return users
    except Exception: 
        raise
    finally:
        cur.close()
        conn.close()

def get_user_by_id(user_id):
    conn = get_db()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT * FROM User WHERE user_id=?", (user_id,))
        user = cur.fetchone()
        return user
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()

def activate_user(user_id, password):
    conn = get_db()
    cur = conn.cursor()
    
    try:
        cur.execute("UPDATE User SET password=?, activated=1 WHERE user_id=?", (password, user_id))
        conn.commit()
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()